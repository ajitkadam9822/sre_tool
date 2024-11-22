import requests
import time

URL="http://localhost:5000"


def fetch_servers():
    response=requests.get(f"{URL}/servers")
    response=response.json()
    print(response)
    return response


def fetch_service_data(ip_address):
    response=requests.get(f"{URL}/{ip_address}")
    response=response.json()
    #print(response)
    return response


def display_services():
    server_list=fetch_servers()
    servicetracker={}
    print(f"{'IP Address':<20} {'Service':<20} {'Status':<10} {'CPU':<10} {'Memory':<10}")
    for ip in server_list:
        data=fetch_service_data(ip)
        health='Healthy'
        
        if(data['service'] in servicetracker):
            servicetracker[data['service']]=servicetracker[data['service']]+1
        if(data['service'] not in servicetracker):    
            servicetracker[data['service']]=1
        if(int(data['cpu'].strip('%'))>80 or int(data['memory'].strip('%'))>80):
            health='Unhealthy'
        
        print(f"{ip:<20} {data['service']:<20} {health:<10} {data['cpu']:<10} {data['memory']:<10}")
    print(servicetracker)
def average_usage():
    server_list=fetch_servers()



def main():
    
    #fetch_servers()    
    fetch_service_data("10.58.1.6")
    display_services()

if __name__ == "__main__":
    main()