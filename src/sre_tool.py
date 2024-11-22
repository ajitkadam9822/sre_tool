import requests
import time
import json

def fetch_servers():
    response=requests.get("http://localhost:5000/servers")
    print(response)

fetch_servers()    