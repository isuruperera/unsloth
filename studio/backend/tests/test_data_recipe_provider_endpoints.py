# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import pytest

from core.data_recipe.service import _validate_provider_endpoint


def test_rejects_non_http_scheme():
    with pytest.raises(ValueError):
        _validate_provider_endpoint("file:///etc/passwd", provider_name = "p")


def test_rejects_link_local_and_loopback_literals():
    with pytest.raises(ValueError):
        _validate_provider_endpoint(
            "http://169.254.169.254/latest/meta-data", provider_name = "p"
        )

    with pytest.raises(ValueError):
        _validate_provider_endpoint("http://127.0.0.1:8000/v1", provider_name = "p")


def test_allowlisted_host_is_accepted(monkeypatch):
    monkeypatch.setenv("UNSLOTH_ALLOWED_PROVIDER_HOSTS", "127.0.0.1")
    assert (
        _validate_provider_endpoint("http://127.0.0.1:8000/v1", provider_name = "p")
        == "http://127.0.0.1:8000/v1"
    )
