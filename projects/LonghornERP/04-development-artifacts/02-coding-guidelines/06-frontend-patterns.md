# Frontend JavaScript Conventions

## One File Per Page

Each page shall have exactly 1 dedicated JavaScript file located at `public/js/[page-name].js`. Logic shall not be split across multiple JS files for a single page, and no JavaScript logic shall be duplicated between page files. Shared utility functions shall reside in `public/js/shared/[util-name].js` and loaded separately.

## No Inline Scripts

PHP template files shall contain no `<script>` tags with inline code. All JavaScript shall be loaded from external `.js` files. The only permitted inline data injection is a `<script>` block that assigns server-side values to a configuration object:

```html
<!-- Acceptable — data injection only, no logic -->
<script>
  const pageConfig = {
    csrfToken: '<?= htmlspecialchars($csrfToken, ENT_QUOTES, "UTF-8") ?>',
    tenantId: <?= (int) $tenantId ?>,
  };
</script>
<script src="/js/invoices-list.js"></script>
```

## API Calls via Fetch

All API calls shall use the native Fetch API with relative paths. `jQuery.ajax()` is prohibited. Relative paths shall target `./api/[domain]/[action].php` from the calling page's directory.

```js
// Correct
const response = await fetch('./api/sales/save-invoice.php', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': pageConfig.csrfToken,
    },
    body: JSON.stringify(payload),
});

// INCORRECT — jQuery AJAX prohibited
$.ajax({ url: './api/sales/save-invoice.php', method: 'POST', ... });
```

## CSRF Token on State-Changing Requests

All non-GET Fetch requests shall include the `X-CSRF-Token` header populated from `pageConfig.csrfToken`. This applies to POST, PUT, PATCH, and DELETE requests.

## User Feedback

All user-facing alerts, confirmations, and notifications shall use SweetAlert2 (`Swal.fire(...)`). Native `alert()`, `confirm()`, and `prompt()` calls are prohibited.

```js
// Correct
Swal.fire({
    icon: 'success',
    title: 'Invoice Saved',
    text: 'Invoice INV-2026-0042 has been saved successfully.',
});

// INCORRECT
alert('Invoice saved.');
```

## DataTables

All tables shall render via DataTables. Tables presenting datasets that may exceed 100 rows shall use server-side processing mode. The DataTables server-side endpoint shall reside in `public/api/[domain]/dt-[entity].php`.

## Select2

All searchable dropdown inputs shall use Select2. Plain `<select>` elements without Select2 are acceptable only for dropdowns with ≤ 5 static options that will never require search.

## Flatpickr

All date inputs shall use Flatpickr for date selection. The display format shall be `d M Y` (e.g., `05 Apr 2026`). The value submitted to the server shall be `Y-m-d`.

```js
flatpickr('#invoice-date', {
    dateFormat: 'Y-m-d',
    altInput: true,
    altFormat: 'd M Y',
});
```

## Icons

All icons shall use Bootstrap Icons via the `bi-[icon-name]` CSS class convention. Font Awesome, Material Icons, and other icon libraries are not permitted in this codebase.

```html
<!-- Correct -->
<i class="bi bi-pencil-square"></i>

<!-- INCORRECT — Font Awesome prohibited -->
<i class="fa fa-edit"></i>
```
