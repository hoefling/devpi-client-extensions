import sys
import pytest
from pkg_resources import DistributionNotFound


class DistMock:
    version = '1.2.3.dev123'


@pytest.fixture
def unload_imports():
    for mod in ('devpi_ext', 'devpi_ext.login'):
        try:
            del sys.modules[mod]
        except KeyError:
            continue


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
