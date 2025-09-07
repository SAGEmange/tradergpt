"""Scaffold to refresh data from external sources."""

"""Scaffold to refresh data from external sources."""

from __future__ import annotations


def fetch_boom500() -> None:
    """Fetch updated Boom500 data from external API."""
    # TODO: implement real data fetching
    pass


def fetch_crash1000() -> None:
    """Fetch updated Crash1000 data from external API."""
    # TODO: implement real data fetching
    pass


def main() -> None:
    """Entrypoint for manual syncing."""
    fetch_boom500()
    fetch_crash1000()


if __name__ == "__main__":  # pragma: no cover
    main()

