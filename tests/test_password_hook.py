import pytest
from devpi_ext import login


@pytest.mark.usefixtures('patched_open_conf_single_section')
def test_password_is_found_in_config():
    assert login.devpiclient_get_password('http://foo', 'bar') == 'baz'

@pytest.mark.usefixtures('patched_open_raises')
def test_password_is_none_when_pypirc_missing():
    assert login.devpiclient_get_password('http://foo', 'bar') is None

@pytest.mark.usefixtures('patched_open_conf_no_repo')
def test_password_is_none_when_repo_missing():
    assert login.devpiclient_get_password('http://foo', 'bar') is None

@pytest.mark.usefixtures('patched_open_conf_no_username')
def test_password_is_none_when_username_missing():
    assert login.devpiclient_get_password('http://foo', 'bar') is None

@pytest.mark.usefixtures('patched_open_conf_no_password')
def test_password_is_none_when_password_missing():
    assert login.devpiclient_get_password('http://foo', 'bar') is None
