# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import pytest
from fastapi import HTTPException

from auth.authentication import _authorize_workspace_owner


def test_authorize_workspace_owner_accepts_matching_subject():
    assert _authorize_workspace_owner("owner", "owner") == "owner"


@pytest.mark.parametrize("workspace_owner", ["different-owner", None])
def test_authorize_workspace_owner_rejects_non_owner(workspace_owner):
    with pytest.raises(HTTPException) as exception_info:
        _authorize_workspace_owner("owner", workspace_owner)

    assert exception_info.value.status_code == 403
