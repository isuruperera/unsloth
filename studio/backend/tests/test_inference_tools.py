# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

from core.inference.tools import _get_workdir_key


def test_workdir_key_is_subject_scoped_and_path_safe():
    session_id = "shared-session"
    first_subject_key = _get_workdir_key("subject-one", session_id)

    assert first_subject_key != _get_workdir_key("subject-two", session_id)
    assert first_subject_key == _get_workdir_key("subject-one", session_id)
    assert "/" not in first_subject_key
    assert "\\" not in first_subject_key
    assert ".." not in first_subject_key
