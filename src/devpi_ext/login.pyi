from typing import Optional, Text, TextIO
from pluggy import HookimplMarker

hookimpl: HookimplMarker

def _find_password(fp: TextIO, url: Text, username: Text) -> Optional[Text]: ...
def devpiclient_get_password(url: Text, username: Text) -> Optional[Text]: ...
