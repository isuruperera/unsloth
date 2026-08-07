# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_bash_exec_uses_allowlist_instead_of_shell_denylist():
    tools_source = (
        Path(__file__).resolve().parent.parent / "core" / "inference" / "tools.py"
    ).read_text()

    assert '["bash", "-c"' not in tools_source
    assert "'bash', '-c'" not in tools_source
    assert "_BASH_BLOCKED_WORDS" not in tools_source
    assert "_BASH_ALLOWED_COMMANDS" in tools_source
    assert "shlex.split(" in tools_source
