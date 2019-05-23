import sys
from devpi.main import get_pluginmanager
from devpi_ext import login
import toml
import pytest
from _pytest import pathlib


@pytest.fixture(scope='session', params=('_pypirc_plugin', '_keyring_plugin'))
def plugin_name(request):
    pyproj = pathlib.Path(__file__, '..', '..', 'pyproject.toml').resolve()
    conf = toml.load(str(pyproj))  # python < 3.6 compat
    return next(
        k
        for k, v in conf['tool']['poetry']['plugins']['devpi_client'].items()
        if v.startswith('{}:{}'.format(login.__name__, request.param))
    )


def test_devpi_ext_plugin_registered(plugin_name):
    pm = get_pluginmanager()
    assert pm.is_registered(pm.get_plugin(plugin_name))


def test_hookimpl_is_tryfirst(plugin_name):
    pm = get_pluginmanager()
    impls = pm.hook.devpiclient_get_password.get_hookimpls()
    print(impls)
    impl = next(i for i in impls if i.plugin_name == plugin_name)
    assert impl.tryfirst is True


@pytest.mark.usefixtures('pypirc')
@pytest.mark.parametrize('plugin', ('_pypirc_plugin', '_keyring_plugin'))
def test_devpi_ext_plugin_hook_called(monkeypatch, plugin):
    monkeypatch.setattr(login, 'get_password', lambda service, user: 'fizz')
    monkeypatch.delattr('devpi.login.devpiclient_get_password')
    plugin_cls = login.__dict__[plugin].__class__
    monkeypatch.delattr(
        '{}.{}.devpiclient_get_password'.format(
            plugin_cls.__module__, plugin_cls.__name__
        )
    )
    pm = get_pluginmanager()
    pw = pm.hook.devpiclient_get_password(url='http://fizz', username='fizz')
    assert pw == 'fizz'
