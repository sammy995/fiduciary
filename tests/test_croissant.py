"""data/croissant.json stays in sync with the scenario set."""
import glob
import json


def test_croissant_metadata_is_present_and_consistent():
    with open("data/croissant.json", encoding="utf-8") as fh:
        meta = json.load(fh)
    assert meta["@type"] == "sc:Dataset"
    assert meta["name"] == "fiduciary-wave1-scenarios"
    assert meta["license"] == "https://www.apache.org/licenses/LICENSE-2.0"
    n_files = len(glob.glob("data/scenarios/wave1/*.yaml"))
    assert meta["fiduciary:scenarioCount"] == n_files
