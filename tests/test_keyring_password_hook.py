try:
    import builtins
except ImportError:
    import __builtin__ as builtins
import pytest


@pytest.fixture
def no_keyring_installed(monkeypatch):
    import_orig = builtins.__import__

    def mocked_import(name, *args):
        if name == 'keyring':
            raise ImportError()
        return import_orig(name, *args)

    with monkeypatch.context() as m:
        m.setattr(builtins, '__import__', mocked_import)
        yield


@pytest.mark.usefixtures('unload_imports', 'no_keyring_installed')
def test_password_is_none_when_keyring_not_importable():
    from devpi_ext import login

    assert login.KeyringPlugin().devpiclient_get_password('http://fizz', 'buzz') is None


@pytest.mark.usefixtures('unload_imports')
def test_password_is_none_when_keyring_misses_credentials(monkeypatch):
    monkeypatch.setattr('keyring.get_password', lambda service, user: None)
    from devpi_ext import login

    assert login.KeyringPlugin().devpiclient_get_password('http://fizz', 'buzz') is None


@pytest.mark.usefixtures('unload_imports')
def test_password_is_found_when_keyring_stores_credentials(monkeypatch):
    monkeypatch.setattr('keyring.get_password', lambda service, user: 'fuzz')
    from devpi_ext import login

    assert (
        login.KeyringPlugin().devpiclient_get_password('http://fizz', 'buzz') == 'fuzz'
    )


def test_printed_message_when_password_is_found_in_keyring(capsys, monkeypatch):
    monkeypatch.setattr('keyring.get_password', lambda service, user: 'fuzz')
    from devpi_ext import login

    login.KeyringPlugin().devpiclient_get_password('http://fizz', 'buzz') == 'fuzz'
    captured = capsys.readouterr()
    assert captured.out == 'Using buzz credentials from keyring\n'
