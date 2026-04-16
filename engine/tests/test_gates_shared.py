from engine.gates._shared import attach_clause, ClauseRef
from engine.findings import Finding, Severity

def test_attach_clause_appends_clause_to_message():
    f = Finding("phase05.test_oracle", Severity.HIGH, "FR-001 has no oracle", None, None)
    f2 = attach_clause(f, ClauseRef("ISO/IEC/IEEE 29119-3", "7.2.3"))
    assert "[ISO/IEC/IEEE 29119-3 §7.2.3]" in f2.message
