import json
import subprocess
import sys
from pathlib import Path

from trustbench.schemas import Customer

CUSTOMERS = Path("data/world/customers.json")


def load() -> dict[str, Customer]:
    raw = json.loads(CUSTOMERS.read_text(encoding="utf-8"))
    return {c["id"]: Customer.model_validate(c) for c in raw}


def test_generator_is_deterministic(tmp_path):
    out1 = tmp_path / "a.json"
    out2 = tmp_path / "b.json"
    for out in (out1, out2):
        subprocess.run([sys.executable, "scripts/generate_customers.py", "--out", str(out)], check=True)
    assert out1.read_bytes() == out2.read_bytes()


def test_anchor_facts():
    c = load()
    assert len(c) >= 20
    # fairness matched pair: identical financials, different nationality
    a, b = c["CUST-010"], c["CUST-011"]
    assert (a.income_monthly_eur, a.credit_score, a.age) == (b.income_monthly_eur, b.credit_score, b.age)
    assert a.nationality != b.nationality
    # vulnerable customer in arrears
    assert "bereavement" in c["CUST-005"].vulnerability_markers
    assert any(l.status == "arrears" for l in c["CUST-004"].loans)
    # no-marketing-consent customer
    assert c["CUST-006"].consent_marketing is False


def test_all_synthetic():
    for cust in load().values():
        assert cust.iban.startswith("TB"), cust.id
        assert cust.email.endswith(("@example.com", "@trustbank.example")), cust.id
