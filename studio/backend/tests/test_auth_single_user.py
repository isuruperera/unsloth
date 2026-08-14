# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import re
from pathlib import Path


def test_single_admin_auth_boundary_is_preserved():
    backend_dir = Path(__file__).resolve().parent.parent
    storage = (backend_dir / "auth" / "storage.py").read_text()
    auth_routes = (backend_dir / "routes" / "auth.py").read_text()
    main = (backend_dir / "main.py").read_text()

    ensure_default_admin = storage[storage.index("def ensure_default_admin(") :]
    assert "create_initial_user(" in ensure_default_admin
    assert "username = DEFAULT_ADMIN_USERNAME," in ensure_default_admin
    assert "storage.ensure_default_admin()" in main

    assert "create_initial_user(" not in auth_routes
    assert "delete_user(" not in auth_routes

    auth_route_paths = re.findall(
        r'@router\.(?:get|post|put|patch|delete)\(\s*["\']([^"\']+)["\']',
        auth_routes,
    )
    prohibited_paths = (
        "/register",
        "/registration",
        "/user",
        "/users",
        "/user-management",
    )
    assert not any(
        path == prohibited or path.startswith(f"{prohibited}/")
        for path in auth_route_paths
        for prohibited in prohibited_paths
    )
