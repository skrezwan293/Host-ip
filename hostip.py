from termcolor import colored
import pyfiglet
import socket

banner = pyfiglet.figlet_format("Host - IP")
print (colored(banner, "cyan"))

def get_ip_address(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

if __name__ == "__main__":
    hostname = (input(colored("Enter the hostname (e.g., www.google.com): ","yellow")))
    ip_address = get_ip_address(hostname)
    
    if ip_address:
        print(colored(f"The IP address of {hostname} is {ip_address}","green"))
    else:
        print(colored(f"Could not retrieve the IP address for {hostname}","red"))
