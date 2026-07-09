from trustbench.world import load_world

EXPECTED_POLICIES = {"POL-001", "POL-002", "POL-003", "POL-004", "POL-005"}
EXPECTED_REGS = {"REG-GDPR", "REG-EUAIACT", "REG-SR117", "REG-PCIDSS", "REG-AMLD", "REG-EBALOM"}


def test_real_world_policies_present():
    world = load_world("data/world")
    assert EXPECTED_POLICIES <= set(world.policies)
    assert EXPECTED_REGS <= set(world.regulations)


def test_policy_bodies_have_sections():
    world = load_world("data/world")
    for pid in EXPECTED_POLICIES:
        assert "## 1." in world.policies[pid].body, f"{pid} missing numbered sections"
