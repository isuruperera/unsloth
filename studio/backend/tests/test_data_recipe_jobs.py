# SPDX-License-Identifier: AGPL-3.0-only
# Copyright 2026-present the Unsloth AI Inc. team. All rights reserved. See /studio/LICENSE.AGPL-3.0

import pytest
from fastapi import HTTPException

from core.data_recipe.jobs.manager import JobManager
from core.data_recipe.jobs.types import Job
from models.data_recipe import PublishDatasetRequest
from routes.data_recipe.jobs import publish_job_dataset


def test_publish_unknown_job_rejects_caller_artifact_path():
    payload = PublishDatasetRequest(
        repo_id = "owner/dataset",
        description = "Dataset description",
        artifact_path = "/caller/supplied/artifact",
    )

    with pytest.raises(HTTPException) as exc_info:
        publish_job_dataset(
            "unknown-job",
            payload,
            current_subject = "test-subject",
        )

    assert exc_info.value.status_code == 404


def test_owner_aware_status_lookup_rejects_different_subject():
    manager = JobManager()
    manager._job = Job(
        job_id = "job-id",
        creator_subject = "creating-subject",
        status = "completed",
    )

    assert manager.get_status("job-id", creator_subject = "creating-subject") is not None
    assert manager.get_status("job-id", creator_subject = "different-subject") is None
