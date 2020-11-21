import sys

import pytest

if sys.version_info >= (3, 8):  # pragma: no cover
    from importlib import metadata as importlib_metadata
else:  # pragma: no cover
    import importlib_metadata


fake_version = '1.2.3.dev123'


@pytest.mark.usefixtures('unload_imports')
def test_version_when_package_installed(monkeypatch):
    # happy testing
    monkeypatch.setattr(
        '{}.version'.format(importlib_metadata.__name__), lambda s: fake_version
    )
    from devpi_ext import __version__

    assert __version__ == fake_version


@pytest.mark.usefixtures('unload_imports')
def test_version_when_reading_raises(monkeypatch):
    def raise_(*args, **kwargs):
        raise importlib_metadata.PackageNotFoundError()

    monkeypatch.setattr('{}.version'.format(importlib_metadata.__name__), raise_)
    from devpi_ext import __version__

    assert __version__ == 'UNKNOWN'
