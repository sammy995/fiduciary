from trustbench.schemas import WAVE1_DIMENSIONS
from trustbench.taxonomy import control_index, load_taxonomy


def test_loads_13_dimensions():
    tax = load_taxonomy()
    assert len(tax.dimensions) == 13
    keys = [d.key for d in tax.dimensions]
    assert keys[:4] == list(WAVE1_DIMENSIONS)


def test_wave1_controls_complete():
    tax = load_taxonomy()
    for d in tax.dimensions:
        if d.key in WAVE1_DIMENSIONS:
            assert d.wave == 1
            assert len(d.controls) == 5, f"{d.key} must have 5 controls"
            for c in d.controls:
                assert c.regulation, f"{c.id} missing regulation mapping"
        else:
            assert d.wave in (2, 3)
            assert len(d.controls) >= 2


def test_control_ids_unique():
    tax = load_taxonomy()
    idx = control_index(tax)
    total = sum(len(d.controls) for d in tax.dimensions)
    assert len(idx) == total
    assert "PRIV-C1" in idx and "FAIR-C5" in idx
