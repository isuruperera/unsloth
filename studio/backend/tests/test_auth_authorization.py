# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import importlib
import unittest


authentication = importlib.import_module("auth.authentication")
storage = importlib.import_module("auth.storage")


class TestAuthorizeSubject(unittest.TestCase):
    def test_allows_default_admin(self):
        assert (
            authentication.authorize_subject(storage.DEFAULT_ADMIN_USERNAME)
            == storage.DEFAULT_ADMIN_USERNAME
        )

    def test_rejects_other_subject(self):
        with self.assertRaises(authentication.HTTPException) as exc_info:
            authentication.authorize_subject("another-user")

        assert exc_info.exception.status_code == 403
