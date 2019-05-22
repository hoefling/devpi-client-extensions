try:
    from StringIO import StringIO  # python2
except ImportError:
    from io import StringIO  # python3

from devpi_ext import login


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


def test_password_is_none_when_pypirc_missing(mocker):
    m = mocker.patch('os.path.isfile')
    m.return_value = False
    assert login.PypircPlugin().devpiclient_get_password('http://foo', 'bar') is None


def test_password_is_none_when_pypirc_not_readable(mocker):
    m = mocker.mock_open()
    m.side_effect = IOError
    mocker.patch('devpi_ext.login.open', m, create=True)
    assert login.PypircPlugin().devpiclient_get_password('http://foo', 'bar') is None


def test_password_is_none_when_pypirc_misses_credentials(mocker):
    m = mocker.mock_open(read_data='\n'.join(section))
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
    mocker.patch('devpi_ext.login.open', m, create=True)
    assert login.PypircPlugin().devpiclient_get_password('http://foo', 'fizz') is None


def test_password_is_found_when_pypirc_present_and_readable(mocker):
    m = mocker.mock_open(read_data='\n'.join(section))
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    m.return_value.__next__ = lambda self: next(iter(self.readline, ''))
    mocker.patch('devpi_ext.login.open', m, create=True)
    assert login.PypircPlugin().devpiclient_get_password('http://foo', 'bar') == 'baz'
