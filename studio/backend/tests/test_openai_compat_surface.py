# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_v1_mount_exposes_only_openai_endpoints():
    main_src = (Path(__file__).resolve().parent.parent / "main.py").read_text()

    assert 'include_router(openai_compat_router, prefix = "/v1"' in main_src
    assert 'include_router(inference_router, prefix = "/v1"' not in main_src
    assert 'include_router(inference_router, prefix = "/api/inference"' in main_src

    inference_src = (
        Path(__file__).resolve().parent.parent / "routes" / "inference.py"
    ).read_text()

    assert '@openai_router.post("/chat/completions")' in inference_src
    assert '@openai_router.get("/models")' in inference_src
    assert '@openai_router.post("/validate")' not in inference_src
