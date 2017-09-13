"""
Defines custom hook for password search. This tries to get credentials
from .pypirc file. Will return nothing if the file is not present
or not well-formed. In that case, the standard hook with entering password
from command line will be used.
"""


from pluggy import HookimplMarker
from devpi.pypirc import Auth


hookimpl = HookimplMarker('devpiclient')


# ---------------------------------------------------------------------
@hookimpl(tryfirst=True)
def devpiclient_get_password(url, username):
    """See :py:func:`devpi.hookspecs.devpiclient_get_password`"""
    try:
        auth = Auth()
    except IOError:
        return None

    password = next((s['password'] for s in auth.ini.sections.values()
                     if all(k in s for k in ('repository', 'username', 'password', ))
                     and s['repository'].startswith(url)
                     and s['username'] == username), None)
    if password:
        print('Using {} credentials from .pypirc'.format(username))
    return password
