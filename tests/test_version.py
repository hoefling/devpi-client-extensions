from pkg_resources import DistributionNotFound

import pytest


class DistMock:
    version = '1.2.3.dev123'


@pytest.mark.usefixtures('unload_imports')
def test_version_when_package_installed(monkeypatch):
    # happy testing
    monkeypatch.setattr('pkg_resources.get_distribution', lambda s: DistMock())
    from devpi_ext import __version__

    assert __version__ == DistMock.version


@pytest.mark.usefixtures('unload_imports')
@pytest.mark.parametrize('error_cls', (DistributionNotFound, ImportError))
def test_version_when_reading_raises(monkeypatch, error_cls):
    def raise_(*args, **kwargs):
        raise error_cls()

    monkeypatch.setattr('pkg_resources.get_distribution', raise_)
    from devpi_ext import __version__

    assert __version__ == 'UNKNOWN'
