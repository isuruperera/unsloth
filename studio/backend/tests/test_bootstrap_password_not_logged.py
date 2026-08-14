# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_bootstrap_password_not_printed_to_stdout():
    main_source = (Path(__file__).resolve().parent.parent / "main.py").read_text()

    assert "password: {bootstrap_pw}" not in main_source
    assert "app.state.bootstrap_password = bootstrap_pw" in main_source
