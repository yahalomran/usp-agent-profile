"""Hosting-repo conformance tests for the committed platform-profile.json."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "platform-profile.json"


def test_keyless_invariant():
    text = ARTIFACT.read_text(encoding="utf-8")
    for key in ("keys", "signing_keys", "webhook_url"):
        assert f'"{key}"' not in text, f"forbidden field {key} present"


def test_build_py_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "build.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_artifact_is_object_with_usp_and_ucp():
    doc = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert "usp" in doc and "ucp" in doc
    assert doc["usp"]["services"] == {"dev.usp.services": [{"transport": "rest"}]}
    assert doc["ucp"]["version"] == "2026-04-08"
    assert "com.stripe" in doc["ucp"]["payment_handlers"]
