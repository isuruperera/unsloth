# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_training_route_preserves_request_trust_remote_code():
    training_route = (
        Path(__file__).resolve().parent.parent / "routes" / "training.py"
    ).read_text()

    assert '"trust_remote_code": request.trust_remote_code' in training_route
    assert "load_model_defaults" not in training_route
    assert 'training_kwargs["trust_remote_code"] = True' not in training_route


def test_training_worker_does_not_auto_enable_remote_code():
    training_worker = (
        Path(__file__).resolve().parent.parent / "core" / "training" / "worker.py"
    ).read_text()

    assert 'config["trust_remote_code"] = True' not in training_worker
    assert 'model_name.lower().startswith("unsloth/")' not in training_worker
