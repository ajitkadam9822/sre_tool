import requests
import time

URL="http://localhost:5000"


def fetch_servers():
    response=requests.get(f"{URL}/servers")
    response=response.json()
    #print(response)
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
    usage_data={}
    for ip in server_list:
        data=fetch_service_data(ip)
        service_name=data["service"]
        cpu=int(data["cpu"].strip('%'))
        memory=int(data["memory"].strip('%'))
        if(service_name not in usage_data):
            usage_data[service_name]={"cpu": [], "memory": []}
        usage_data[service_name]['cpu'].append(cpu)
        usage_data[service_name]['memory'].append(memory)  

    for service,data in usage_data.items():
        avg_cpu=sum(data["cpu"])/len(data["cpu"])
        avg_memory=sum(data["memory"])/len(data["memory"])
        avg_cpu=round(avg_cpu,2)
        avg_memory=round(avg_memory,2)
        print(f"{service:<20} Average CPU={avg_cpu:}% {'  '}Average Memory={avg_memory:}%")   
         



def check_health():
    server_list=fetch_servers()
    health_data={}
    
    for ip in server_list:
        data=fetch_service_data(ip)
        service_name=data["service"]
        cpu=int(data["cpu"].strip('%'))
        memory=int(data["memory"].strip('%'))
        if service_name not in health_data:
            health_data[service_name]=0
        if cpu<80 and memory<80:
            health_data[service_name]=health_data[service_name]+1  
        for service,count in health_data.items():
            unhealthy_service_flag=0
            if count<2:
                unhealthy_service_flag=1
                print(f"WARNING: {service} has fewer than 2 healthy instances!")      
            if unhealthy_service_flag==0:
                 print("\nNo Unhealthy Service found!")
def track_service(service_name):
    try:
        
        while True:
            servers=fetch_servers()
            instance_count=0
           
            for ip in servers:
                data=fetch_service_data(ip)
                if (data['service']==service_name):
                    health="Healthy"
                    instance_count=instance_count+1
                    if(int(data['cpu'].strip('%'))>80 or int(data['memory'].strip('%'))>80):
                        health='Unhealthy'
                    print(f"IP={ip:<15} CPU={data['cpu']:<10} Memory={data['memory']:<10} {health:<10}")        
            print(f"Total instances running:{instance_count}")
            time.sleep(5)
    except KeyboardInterrupt:
        
        print("\nStopped tracking service.")        


def main():
    
   while True:
        print("\nChoose an action:")
        print("1. List all running services")
        print("2. Calculate average CPU/Memory usage by service")
        print("3. Check health of services")
        print("4. Track a specific service")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice=="1":
            display_services()
        elif choice=="2":    
            average_usage()
        elif choice=="3":
            check_health()
        elif choice=="4":
            service_name = input("Enter the service name to track: ")
            track_service(service_name)
        elif choice=="5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()