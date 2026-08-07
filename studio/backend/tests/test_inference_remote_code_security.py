# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


BACKEND_ROOT = Path(__file__).resolve().parent.parent


def test_openai_compat_routes_cannot_load_remote_code():
    main_source = (BACKEND_ROOT / "main.py").read_text()
    inference_source = (BACKEND_ROOT / "routes" / "inference.py").read_text()
    model_source = (BACKEND_ROOT / "models" / "inference.py").read_text()

    assert 'app.include_router(inference_router, prefix = "/api/inference"' in main_source
    assert 'app.include_router(inference_router, prefix = "/v1"' not in main_source
    assert 'app.include_router(openai_router, prefix = "/v1"' in main_source
    assert '@openai_router.post("/chat/completions")' in inference_source
    assert '@openai_router.get("/models")' in inference_source
    assert "trust_remote_code:" not in model_source
    assert "trust_remote_code = False" in inference_source
