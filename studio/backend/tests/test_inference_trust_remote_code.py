# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_load_model_derives_trust_remote_code_from_server_defaults():
    inference_route = (
        Path(__file__).resolve().parent.parent / "routes" / "inference.py"
    ).read_text()

    assert "trust_remote_code = request.trust_remote_code" not in inference_route
    assert "load_model_defaults(config.identifier)" in inference_route
    assert "trust_remote_code = allow_remote_code" in inference_route
