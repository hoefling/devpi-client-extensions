# pyre-strict

"""
Defines custom hook for password search. This tries to get credentials
from .pypirc file. Will return nothing if the file is not present
or not well-formed. In that case, the standard hook with entering password
from command line will be used.
"""


try:
    import configparser
except ImportError:  # pragma: no cover
    # python2 compat
    import ConfigParser as configparser
import os

try:
    from keyring import get_password
except ImportError:

    def get_password(service_name, username):
        return None


import devpi.main


_key_repo = 'repository'
_key_username = 'username'
_key_password = 'password'
_section_keys = (_key_repo, _key_username, _key_password)


class PypircPlugin:
    @devpi.main.hookimpl(tryfirst=True)
    def devpiclient_get_password(self, url, username):
        """See :py:func:`devpi.hookspecs.devpiclient_get_password`"""
        pypirc = os.path.join(os.path.expanduser('~'), '.pypirc')
        try:
            with open(pypirc) as fp:
                password = _find_password(fp, url, username)
        except (OSError, IOError):
            return None

        if password:
            print('Using {} credentials from .pypirc'.format(username))
        return password


def _find_password(fp, url, username):
    """Parses config from file-like object and searches for a password."""
    parser = configparser.ConfigParser()
    parser.read_file(fp)
    sections = (dict(parser.items(name)) for name in parser.sections())
    return next(
        (
            s[_key_password]
            for s in sections
            if all(k in s for k in _section_keys)
            and s[_key_repo].startswith(url)
            and s[_key_username] == username
        ),
        None,
    )


class KeyringPlugin:
    @devpi.main.hookimpl(tryfirst=True)
    def devpiclient_get_password(self, url, username):
        password = get_password(url, username)
        if password:
            print('Using {} credentials from keyring'.format(username))
        return password


_pypirc_plugin = PypircPlugin()
_keyring_plugin = KeyringPlugin()
