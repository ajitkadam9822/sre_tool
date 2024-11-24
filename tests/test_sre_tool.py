import pytest
import sys

import sre_tool as tool

def test_fetch_servers():
    result=tool.fetch_servers()
    assert result is not None

def test_fetch_service_data():
    server=tool.fetch_servers()
    result=tool.fetch_service_data(server[1])
    if result:
        assert True
    else:
        assert False  

def test_fetch_service_data_with_invalid_value():
    result=tool.fetch_service_data('gdfg')
    if('error' in result):
        assert True
    else:
        assert False  

def test_display_services():
    result=tool.fetch_servers()
    assert len(result)>0

def test_average_usage(capsys):
    tool.average_usage()
    captured=capsys.readouterr()
    
    assert "Average" in str(captured) 

def test_check_health(capsys):
    result=tool.check_health()
    captured=capsys.readouterr()
    assert ("healthy" in str(captured) or "Unhealthy" in str(captured))

def test_track_service(capsys):
    try:      
        tool.track_service('IdService')
        captured=capsys.readouterr()
    except KeyboardInterrupt:
        pass    
   
    assert "CPU" in str(captured) 

    