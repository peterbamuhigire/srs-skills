# 2. Kotlin (Android) Coding Standards

## 2.1 Naming Conventions

| Construct | Convention | Example |
|---|---|---|
| Class | `PascalCase` | `SalesViewModel`, `InvoiceRepository` |
| Interface | `PascalCase` | `InvoiceRepository` (no `I` prefix — Kotlin convention) |
| Function | `camelCase` | `submitRemittance()` |
| Property | `camelCase` | `agentCashBalance` |
| Constant | `UPPER_SNAKE_CASE` in `companion object` | `MAX_RETRY_ATTEMPTS` |
| Composable function | `PascalCase` | `AgentDashboardScreen()`, `CashBalanceCard()` |
| State class | `PascalCase` + `UiState` suffix | `AgentDashboardUiState` |
| ViewModel | `PascalCase` + `ViewModel` suffix | `AgentDashboardViewModel` |
| Repository | `PascalCase` + `Repository` suffix | `InvoiceRepository` (interface), `InvoiceRepositoryImpl` (implementation) |

## 2.2 Jetpack Compose Best Practices

### Composable Functions

```kotlin
@Composable
fun AgentDashboardScreen(
    viewModel: AgentDashboardViewModel = hiltViewModel(),
    onNavigateToNewSale: () -> Unit,
    onNavigateToRemittance: () -> Unit,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    AgentDashboardContent(
        uiState = uiState,
        onNewSaleClick = onNavigateToNewSale,
        onRemittanceClick = onNavigateToRemittance,
        onRefresh = viewModel::refresh,
    )
}

// Separate stateless content composable — testable without ViewModel
@Composable
private fun AgentDashboardContent(
    uiState: AgentDashboardUiState,
    onNewSaleClick: () -> Unit,
    onRemittanceClick: () -> Unit,
    onRefresh: () -> Unit,
) {
    when (uiState) {
        is AgentDashboardUiState.Loading -> LoadingIndicator()
        is AgentDashboardUiState.Success -> DashboardCards(data = uiState.data, ...)
        is AgentDashboardUiState.Error -> ErrorCard(message = uiState.message, onRetry = onRefresh)
    }
}
```

**Compose rules:**

- Every screen Composable has a stateful version (reads from ViewModel) and a stateless content version (receives data as parameters). The stateless version is used in Compose previews and tests.
- `@Preview` annotations are required for all leaf UI components (cards, buttons, form fields).
- Composable functions must not perform side effects directly — use `LaunchedEffect`, `SideEffect`, or `DisposableEffect`.
- `remember { }` and `rememberSaveable { }` are used appropriately. State that must survive configuration changes uses `rememberSaveable`.
- Navigation is handled by the Compose Navigation component. Navigation calls are passed as lambda parameters — Composables never reference `NavController` directly.

### UiState Sealed Class Pattern

```kotlin
sealed class AgentDashboardUiState {
    object Loading : AgentDashboardUiState()
    data class Success(
        val cashBalance: Long,           // UGX in smallest unit (shillings, no decimal)
        val outstandingInvoices: Int,
        val outstandingAmount: Long,
        val lastRemittanceDate: LocalDate?,
        val recentSales: List<SaleSummary>,
    ) : AgentDashboardUiState()
    data class Error(val message: String) : AgentDashboardUiState()
}
```

## 2.3 Repository Pattern (Android)

```kotlin
interface InvoiceRepository {
    suspend fun getInvoicesByAgent(agentId: Int): List<Invoice>
    suspend fun createSale(sale: SaleRequest): Result<Sale>
    fun observeAgentCashBalance(agentId: Int): Flow<Long>
}

class InvoiceRepositoryImpl @Inject constructor(
    private val remoteDataSource: InvoiceRemoteDataSource,
    private val localDataSource: InvoiceLocalDataSource,  // Room DAO
) : InvoiceRepository {

    override suspend fun createSale(sale: SaleRequest): Result<Sale> {
        // Always write to Room first (offline-first, DC-005)
        val localId = localDataSource.insertPendingSale(sale.toEntity())

        return try {
            val remoteSale = remoteDataSource.createSale(sale)
            localDataSource.markSynced(localId, remoteSale.id)
            Result.success(remoteSale)
        } catch (e: IOException) {
            // Network error — sale is safe in Room, WorkManager will sync later
            Result.success(Sale.fromLocalEntity(localDataSource.getById(localId)))
        }
    }
}
```

## 2.4 Coroutines Usage

- All repository and data source functions that perform I/O are `suspend` functions.
- ViewModels launch coroutines in `viewModelScope`. Never use `GlobalScope`.
- Use `Dispatchers.IO` for database and network operations. Never perform I/O on `Dispatchers.Main`.
- Structured concurrency: coroutines are always launched inside a scope that respects lifecycle.

```kotlin
class AgentDashboardViewModel @Inject constructor(
    private val invoiceRepository: InvoiceRepository,
    private val agentRepository: AgentRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow<AgentDashboardUiState>(AgentDashboardUiState.Loading)
    val uiState: StateFlow<AgentDashboardUiState> = _uiState.asStateFlow()

    init {
        loadDashboard()
    }

    fun refresh() {
        loadDashboard()
    }

    private fun loadDashboard() {
        viewModelScope.launch {
            _uiState.value = AgentDashboardUiState.Loading
            try {
                val agentId = agentRepository.getCurrentAgentId()
                val cashBalance = invoiceRepository.getAgentCashBalance(agentId)
                _uiState.value = AgentDashboardUiState.Success(
                    cashBalance = cashBalance,
                    // ...
                )
            } catch (e: Exception) {
                _uiState.value = AgentDashboardUiState.Error(
                    message = "Could not load dashboard. Pull down to retry."
                )
            }
        }
    }
}
```

## 2.5 Error Handling and Null Safety

- Use Kotlin `Result<T>` for operations that can fail with a business error.
- Use `null` returns (not exceptions) for "not found" scenarios.
- Avoid `!!` (double-bang / non-null assertion operator) except where the compiler cannot infer non-nullability and the null state is architecturally impossible. Every use of `!!` requires a comment explaining why.
- Use `?.let { }`, `?: return`, and `?: throw` for null handling at call sites.

```kotlin
// PROHIBITED — !! without justification
val agent = agentRepository.findById(agentId)!!

// REQUIRED — explicit null handling
val agent = agentRepository.findById(agentId)
    ?: throw AgentNotFoundException("Agent ID $agentId not found")
```

## 2.6 Monetary Values

All monetary amounts in Uganda Shillings (UGX) are stored and manipulated as `Long` (integer shillings). Never use `Float` or `Double` for monetary values.

Formatting for display uses a helper function:

```kotlin
fun Long.toUgxDisplay(): String = "UGX ${NumberFormat.getNumberInstance().format(this)}"
// Output: "UGX 1,250,000"
```

Room stores monetary amounts as `INTEGER` columns. API JSON responses carry amounts as integer strings (not floating-point numbers) to avoid JSON floating-point precision loss.
