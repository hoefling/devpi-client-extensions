import pytest

section = [
    '[foo]',
    'repository: http://foo',
    'username: bar',
    'password: baz',
]

@pytest.fixture()
def patched_open_raises(mocker):
    conf = '\n'.join(section)
    m = mocker.mock_open(read_data=conf)
    m.side_effect = IOError
    mocker.patch('py._iniconfig.open', m, create=True)

@pytest.fixture()
def patched_open_conf_single_section(mocker):
    conf = '\n'.join(section)
    m = mocker.mock_open(read_data=conf)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('py._iniconfig.open', m, create=True)

@pytest.fixture()
def patched_open_conf_no_repo(mocker):
    conf = '\n'.join(line for line in section if not line.startswith('repository:'))
    m = mocker.mock_open(read_data=conf)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('py._iniconfig.open', m, create=True)

@pytest.fixture()
def patched_open_conf_no_username(mocker):
    conf = '\n'.join(line for line in section if not line.startswith('username:'))
    m = mocker.mock_open(read_data=conf)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('py._iniconfig.open', m, create=True)

@pytest.fixture()
def patched_open_conf_no_password(mocker):
    conf = '\n'.join(line for line in section if not line.startswith('password:'))
    m = mocker.mock_open(read_data=conf)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('py._iniconfig.open', m, create=True)

