The project includes a python script(sre_tool.py), a mock server file(cpx_server.py) and tests.

Instructions:

1. Start the server: 
    python src/cpx_server.py 5000

2. Start the monitoring tool:
    python src/sre_tool.py 

3. For testing :
    pytest tests/

    Ensure you press ctrl+c to complete the tests as the track service function will monitor indefinitely if not interrupted!