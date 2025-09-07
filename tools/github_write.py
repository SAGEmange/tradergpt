"""Helper utilities for writing files via the GitHub Contents API."""

from __future__ import annotations

import base64
import os
from typing import Optional

import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER", "SAGEmange")
GITHUB_REPO = os.getenv("GITHUB_REPO", "trader-signals-repo")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")
API_ROOT = "https://api.github.com"


class GitHubError(RuntimeError):
    """Raised when the GitHub API returns an error."""


def _headers() -> dict[str, str]:
    if not GITHUB_TOKEN:
        raise GitHubError("GITHUB_TOKEN not set")
    return {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }


def get_file_sha(path: str) -> Optional[str]:
    """Return the SHA of *path* on GitHub or ``None`` if missing."""
    url = f"{API_ROOT}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}?ref={GITHUB_BRANCH}"
    r = requests.get(url, headers=_headers())
    if r.status_code == 200:
        return r.json().get("sha")
    if r.status_code == 404:
        return None
    raise GitHubError(f"Error fetching SHA: {r.text}")


def put_file(path: str, content_bytes: bytes, message: str, sha: Optional[str] = None) -> dict:
    """Create or update *path* with *content_bytes* and commit *message*."""
    url = f"{API_ROOT}/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{path}"
    data: dict[str, object] = {
        "message": message,
        "content": base64.b64encode(content_bytes).decode(),
        "branch": GITHUB_BRANCH,
    }
    if sha:
        data["sha"] = sha
    r = requests.put(url, headers=_headers(), json=data)
    if r.status_code not in {200, 201}:
        raise GitHubError(f"Error writing file: {r.text}")
    return r.json()


if __name__ == "__main__":  # pragma: no cover
    example = {
        "date": "2025-09-07",
        "wins": 2,
        "losses": 1,
        "survival_pct": 100.0,
        "net_pnl": 0.30,
        "notes": "Lite mode only. Followed SL/TP discipline; no overtrading."
    }
    import json

    sha = get_file_sha("logs/2025-09-07-recap.json")
    put_file(
        "logs/2025-09-07-recap.json",
        json.dumps(example, indent=2).encode(),
        "chore: add recap 2025-09-07",
        sha=sha,
    )

