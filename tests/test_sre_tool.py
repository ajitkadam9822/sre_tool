import pytest
import unittest.mock as mock

import sre_tool as tool

def test_fetch_servers():
    result=tool.fetch_servers()
    assert result is not None


def test_fetch_service_data_with_invalid_value():
    result=tool.fetch_service_data('gdfg')
    if('error' in result):
        assert True
    else:
        assert False  


@mock.patch("sre_tool.fetch_service_data")

def test_fetch_service_data_mock(mock_fetch_data):
    mock_fetch_data.return_value={"cpu":"61%","service":"UserService","memory":"4%"}
    data=tool.fetch_service_data(192)

    assert data=={"cpu":"61%","service":"UserService","memory":"4%"}