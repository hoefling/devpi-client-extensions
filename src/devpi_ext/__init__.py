# pyre-strict

"""Provides version information read from package metadata."""

import sys

if sys.version_info >= (3, 8):  # pragma: no cover
    from importlib import metadata as importlib_metadata
else:  # pragma: no cover
    import importlib_metadata


def _read_version() -> str:
    try:
        return importlib_metadata.version("devpi-client-extensions")
    except importlib_metadata.PackageNotFoundError:
        return "UNKNOWN"


__version__: str = _read_version()
__all__ = ["__version__"]
