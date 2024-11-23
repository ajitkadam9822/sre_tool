The project includes a python script(sre_tool.py), a mock server file(cpx_server.py) and tests.

Features:
1. Print running data about services and their health status. 

2. Print out average CPU/Memory of services of the same type.

3. Flag services which have fewer than 2 healthy instances.

4. Have the ability to track and print CPU/Memory of all instances of a given service over time.

Instructions:

1. Start the server: 
    python src/cpx_server.py 5000

2. Start the monitoring tool:
    python src/sre_tool.py 

3. For testing :
    pytest tests/

    Ensure you press ctrl+c to complete the tests as the track service function will monitor indefinitely if not interrupted!