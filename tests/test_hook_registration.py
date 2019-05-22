from devpi.main import get_pluginmanager
from devpi_ext import login
import toml
import pytest
from _pytest import pathlib

try:
    import configparser
except ImportError:  # pragma: no cover
    # python2 compat
    import ConfigParser as configparser


@pytest.fixture(scope='session')
def plugin_name():
    pyproj = pathlib.Path(__file__, '..', '..', 'pyproject.toml').resolve()
    conf = toml.load(str(pyproj))  # python < 3.6 compat
    return next(
        k
        for k, v in conf['tool']['poetry']['plugins']['devpi_client'].items()
        if v == login.__name__ + ':_pypirc'
    )


@pytest.fixture
def pypirc(monkeypatch, tmp_path):
    parser = configparser.ConfigParser()
    parser.read_dict(
        {
            'distutils': {'index-servers': '\nfizz'},
            'fizz': {
                'repository': 'http://fizz',
                'username': 'fizz',
                'password': 'fizz',
            },
        }
    )
    pypirc = tmp_path / '.pypirc'
    with pypirc.open('w', encoding='utf-8') as fp:
        parser.write(fp)
    with monkeypatch.context() as m:
        m.setattr('os.path.expanduser', lambda *args: str(tmp_path))
        yield


def test_devpi_ext_plugin_registered(plugin_name):
    pm = get_pluginmanager()
    assert pm.is_registered(pm.get_plugin(plugin_name))


def test_get_password_pypirc_hookimpl_is_tryfirst(plugin_name):
    pm = get_pluginmanager()
    impls = pm.hook.devpiclient_get_password.get_hookimpls()
    impl = next(i for i in impls if i.plugin_name == plugin_name)
    assert impl.tryfirst is True


@pytest.mark.usefixtures('pypirc')
def test_get_password_pypirc_hook_called(monkeypatch):
    monkeypatch.delattr('devpi.login.devpiclient_get_password')
    pm = get_pluginmanager()
    pw = pm.hook.devpiclient_get_password(url='http://fizz', username='fizz')
    assert pw == 'fizz'
