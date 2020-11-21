# pyre-strict

"""
Defines custom hook for password search.

This tries to get credentials from :file:`.pypirc` file. Will return nothing
if the file is not present or not well-formed. In that case, the standard hook
with entering password from command line will be used.
"""


import configparser
from pathlib import Path
from typing import Iterable, Optional

import devpi.main

try:
    from keyring import get_password
except ImportError:

    def get_password(service_name: str, username: str) -> Optional[str]:
        """Keyring dummy replacement if ``keyring`` is not installed."""
        return None


_key_repo = 'repository'
_key_username = 'username'
_key_password = 'password'  # nosec
_section_keys = (_key_repo, _key_username, _key_password)


class PypircPlugin:
    """Plugin that implements reading the password from :file:`.pypirc` file."""

    @devpi.main.hookimpl(tryfirst=True)
    def devpiclient_get_password(self, url: str, username: str) -> Optional[str]:
        """.. seealso:: :py:func:`devpi.hookspecs.devpiclient_get_password`."""
        pypirc = Path.home() / '.pypirc'
        try:
            with pypirc.open() as fp:
                password = _find_password(fp, url, username)
        except OSError:
            return None

        if password:
            print('Using {} credentials from .pypirc'.format(username))
        return password


def _find_password(fp: Iterable[str], url: str, username: str) -> Optional[str]:
    """Parse config from file-like object and search for a password."""
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
    """Plugin that implements reading the password from ``keyring`` backend."""

    @devpi.main.hookimpl(tryfirst=True)
    def devpiclient_get_password(self, url: str, username: str) -> Optional[str]:
        """.. seealso:: :py:func:`devpi.hookspecs.devpiclient_get_password`."""
        password = get_password(url, username)
        if password:
            print('Using {} credentials from keyring'.format(username))
        return password


_pypirc_plugin = PypircPlugin()
_keyring_plugin = KeyringPlugin()
