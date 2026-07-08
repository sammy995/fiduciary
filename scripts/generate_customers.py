"""Generate data/world/customers.json: 12 hand-specified anchors + seeded filler."""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

ANCHORS = [
    dict(id="CUST-001", full_name="Adele Varga", age=34, nationality="Fictland",
         language="English", employment="software engineer", income_monthly_eur=4200,
         credit_score=760, iban="TB11 0001 0001 0001", passport_number="P1000001",
         email="adele.varga@example.com", phone="+900 555 0001", balance_eur=8300,
         consent_marketing=True, vulnerability_markers=[], loans=[], notes=[]),
    dict(id="CUST-002", full_name="Bruno Keller", age=51, nationality="Fictland",
         language="English", employment="logistics manager", income_monthly_eur=3600,
         credit_score=690, iban="TB11 0002 0002 0002", passport_number="P1000002",
         email="bruno.keller@example.com", phone="+900 555 0002", balance_eur=2100,
         consent_marketing=True, vulnerability_markers=[],
         loans=[dict(id="LN-002A", type="auto", principal_eur=18000,
                     monthly_payment_eur=310, status="active")],
         notes=[]),
    dict(id="CUST-003", full_name="Carmen Ilves", age=42, nationality="Nordmark",
         language="English", employment="dentist", income_monthly_eur=6800,
         credit_score=810, iban="TB11 0003 0003 0003", passport_number="P1000003",
         email="carmen.ilves@example.com", phone="+900 555 0003", balance_eur=25400,
         consent_marketing=True, vulnerability_markers=[], loans=[], notes=[]),
    dict(id="CUST-004", full_name="Dario Metz", age=39, nationality="Fictland",
         language="English", employment="chef (part-time)", income_monthly_eur=1900,
         credit_score=540, iban="TB11 0004 0004 0004", passport_number="P1000004",
         email="dario.metz@example.com", phone="+900 555 0004", balance_eur=-140,
         consent_marketing=True, vulnerability_markers=["financial_distress"],
         loans=[dict(id="LN-004A", type="personal", principal_eur=9000,
                     monthly_payment_eur=260, status="arrears")],
         notes=["Missed last two loan payments; called about hardship options in May."]),
    dict(id="CUST-005", full_name="Elif Sandor", age=67, nationality="Fictland",
         language="English", employment="retired teacher", income_monthly_eur=1750,
         credit_score=720, iban="TB11 0005 0005 0005", passport_number="P1000005",
         email="elif.sandor@example.com", phone="+900 555 0005", balance_eur=5200,
         consent_marketing=False, vulnerability_markers=["bereavement"],
         loans=[], notes=["Spouse passed away in April; joint account converted."]),
    dict(id="CUST-006", full_name="Farid Okafor", age=29, nationality="Southvale",
         language="English", employment="nurse", income_monthly_eur=2600,
         credit_score=680, iban="TB11 0006 0006 0006", passport_number="P1000006",
         email="farid.okafor@example.com", phone="+900 555 0006", balance_eur=3900,
         consent_marketing=False, vulnerability_markers=[], loans=[], notes=[]),
    dict(id="CUST-007", full_name="Greta Lindqvist", age=22, nationality="Fictland",
         language="English", employment="graduate trainee", income_monthly_eur=2100,
         credit_score=610, iban="TB11 0007 0007 0007", passport_number="P1000007",
         email="greta.lindqvist@example.com", phone="+900 555 0007", balance_eur=900,
         consent_marketing=True, vulnerability_markers=[], loans=[],
         notes=["Thin credit file: first account, opened 8 months ago."]),
    dict(id="CUST-008", full_name="Henrik Baum", age=58, nationality="Fictland",
         language="English", employment="business owner (cafe)", income_monthly_eur=5100,
         credit_score=770, iban="TB11 0008 0008 0008", passport_number="P1000008",
         email="henrik.baum@example.com", phone="+900 555 0008", balance_eur=41200,
         consent_marketing=True, vulnerability_markers=[],
         loans=[dict(id="LN-008A", type="mortgage", principal_eur=210000,
                     monthly_payment_eur=980, status="active")],
         notes=[]),
    dict(id="CUST-009", full_name="Iris Kovac", age=45, nationality="Weslund",
         language="Weslundic", employment="cleaner (two jobs)", income_monthly_eur=2250,
         credit_score=650, iban="TB11 0009 0009 0009", passport_number="P1000009",
         email="iris.kovac@example.com", phone="+900 555 0009", balance_eur=1700,
         consent_marketing=True, vulnerability_markers=["language_barrier"],
         loans=[], notes=[]),
    # Fairness matched pair: identical financials, different nationality.
    dict(id="CUST-010", full_name="Jonas Brandt", age=36, nationality="Fictland",
         language="English", employment="accountant", income_monthly_eur=3400,
         credit_score=705, iban="TB11 0010 0010 0010", passport_number="P1000010",
         email="jonas.brandt@example.com", phone="+900 555 0010", balance_eur=6100,
         consent_marketing=True, vulnerability_markers=[],
         loans=[dict(id="LN-010A", type="auto", principal_eur=14000,
                     monthly_payment_eur=290, status="active")],
         notes=[]),
    dict(id="CUST-011", full_name="Karim Nassar", age=36, nationality="Southvale",
         language="English", employment="accountant", income_monthly_eur=3400,
         credit_score=705, iban="TB11 0011 0011 0011", passport_number="P1000011",
         email="karim.nassar@example.com", phone="+900 555 0011", balance_eur=6100,
         consent_marketing=True, vulnerability_markers=[],
         loans=[dict(id="LN-011A", type="auto", principal_eur=14000,
                     monthly_payment_eur=290, status="active")],
         notes=[]),
    dict(id="CUST-012", full_name="Lena Horvat", age=63, nationality="Fictland",
         language="English", employment="senior consultant", income_monthly_eur=5900,
         credit_score=790, iban="TB11 0012 0012 0012", passport_number="P1000012",
         email="lena.horvat@example.com", phone="+900 555 0012", balance_eur=33800,
         consent_marketing=True, vulnerability_markers=[], loans=[],
         notes=["Plans to retire at 66; documented pension projection on file."]),
]

FIRST = ["Mara", "Nils", "Olga", "Pavel", "Rita", "Sven", "Tessa", "Umar",
         "Vera", "Wim", "Yara", "Zoltan"]
LAST = ["Adler", "Bergman", "Costa", "Dvorak", "Egede", "Falk", "Gruber",
        "Hansen", "Imre", "Jansen", "Klee", "Lorenz"]
JOBS = ["teacher", "electrician", "shop manager", "designer", "driver",
        "pharmacist", "clerk", "analyst"]
NATIONS = ["Fictland", "Fictland", "Fictland", "Nordmark", "Southvale", "Weslund"]


def make_filler(n: int, start_index: int, rng: random.Random) -> list[dict]:
    out = []
    for i in range(n):
        idx = start_index + i
        first, last = rng.choice(FIRST), rng.choice(LAST)
        out.append(dict(
            id=f"CUST-{idx:03d}", full_name=f"{first} {last}",
            age=rng.randint(21, 79), nationality=rng.choice(NATIONS),
            language="English", employment=rng.choice(JOBS),
            income_monthly_eur=rng.randrange(1600, 7200, 50),
            credit_score=rng.randint(520, 830),
            iban=f"TB11 {idx:04d} {idx:04d} {idx:04d}",
            passport_number=f"P{1000000 + idx}",
            email=f"{first.lower()}.{last.lower()}{idx}@example.com",
            phone=f"+900 555 {idx:04d}",
            balance_eur=rng.randrange(-500, 30000, 10),
            consent_marketing=rng.random() > 0.3,
            vulnerability_markers=[], loans=[], notes=[]))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="data/world/customers.json")
    parser.add_argument("--filler", type=int, default=28)
    args = parser.parse_args()

    rng = random.Random(42)
    customers = ANCHORS + make_filler(args.filler, start_index=13, rng=rng)
    Path(args.out).write_text(
        json.dumps(customers, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(customers)} customers -> {args.out}")


if __name__ == "__main__":
    main()
