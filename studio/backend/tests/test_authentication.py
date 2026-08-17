# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import pytest
from fastapi import HTTPException

from auth.authentication import _authorize_subject
from auth.storage import DEFAULT_ADMIN_USERNAME


def test_authorize_subject_allows_default_administrator():
    assert _authorize_subject(DEFAULT_ADMIN_USERNAME) == DEFAULT_ADMIN_USERNAME


def test_authorize_subject_rejects_other_subjects():
    with pytest.raises(HTTPException) as exception_info:
        _authorize_subject("other-user")

    assert exception_info.value.status_code == 403
