import pytest
from devpi_ext import login

try:
    from StringIO import StringIO  # python2
    import __builtin__ as builtins
except ImportError:
    from io import StringIO  # python3
    import builtins


section = ['[foo]', 'repository: http://foo', 'username: bar', 'password: baz']


def test_password_is_found_in_config():
    fp = StringIO('\n'.join(section))
    assert login._find_password(fp, 'http://foo', 'bar') == 'baz'


def test_password_is_none_when_repo_missing():
    fp = StringIO(
        '\n'.join(line for line in section if not line.startswith('repository:'))
    )
    assert login._find_password(fp, 'http://foo', 'bar') is None


def test_password_is_none_when_username_missing():
    fp = StringIO(
        '\n'.join(line for line in section if not line.startswith('username:'))
    )
    assert login._find_password(fp, 'http://foo', 'bar') is None


def test_password_is_none_when_password_missing():
    fp = StringIO(
        '\n'.join(line for line in section if not line.startswith('password:'))
    )
    assert login._find_password(fp, 'http://foo', 'bar') is None


def test_password_is_none_when_pypirc_missing(monkeypatch, tmp_path):
    monkeypatch.setattr('os.path.expanduser', lambda *args: str(tmp_path))
    assert (tmp_path / '.pypirc').is_file() is False
    assert login.PypircPlugin().devpiclient_get_password('http://fizz', 'fizz') is None


def test_password_is_none_when_pypirc_not_readable(monkeypatch):
    def open_(*args, **kwargs):
        raise IOError()

    monkeypatch.setattr(builtins, 'open', open_)
    assert login.PypircPlugin().devpiclient_get_password('http://fizz', 'fizz') is None


@pytest.mark.usefixtures('pypirc')
def test_password_is_none_when_pypirc_misses_credentials():
    assert (
        login.PypircPlugin().devpiclient_get_password('http://missing', 'missing')
        is None
    )


@pytest.mark.usefixtures('pypirc')
def test_password_is_found_when_pypirc_present_and_readable(mocker):
    assert (
        login.PypircPlugin().devpiclient_get_password('http://fizz', 'fizz') == 'fizz'
    )
