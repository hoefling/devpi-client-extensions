import sys
import pytest


try:
    import configparser
except ImportError:  # pragma: no cover
    # python2 compat
    import ConfigParser as configparser


@pytest.fixture
def unload_imports():
    for mod in ('devpi_ext', 'devpi_ext.login'):
        try:
            del sys.modules[mod]
        except KeyError:
            continue


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
