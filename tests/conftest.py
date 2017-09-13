import pytest

conf_single_section = '''
[foo]
repository: http://foo
username: bar
password: baz
'''

@pytest.fixture()
def patched_open(mocker):
    m = mocker.mock_open(read_data=conf_single_section)
    m.return_value.__iter__ = lambda self: iter(self.readline, '')
    mocker.patch('py._iniconfig.open', m, create=True)

@pytest.fixture()
def patched_open_raises(mocker):
    m = mocker.mock_open(read_data=conf_single_section)
    m.side_effect = IOError
    mocker.patch('py._iniconfig.open', m, create=True)
