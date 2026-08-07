# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from pathlib import Path


def test_start_training_never_elevates_trust_remote_code():
    training_route = (
        Path(__file__).resolve().parent.parent / "routes" / "training.py"
    ).read_text()

    assert 'training_kwargs["trust_remote_code"] = True' not in training_route


def test_worker_never_auto_elevates_trust_remote_code_for_unsloth_models():
    worker_source = (
        Path(__file__).resolve().parent.parent / "core" / "training" / "worker.py"
    ).read_text()

    assert 'config["trust_remote_code"] = True' not in worker_source
