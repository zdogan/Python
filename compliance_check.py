
# Calls the intrusion_detection, compliance_checks, and network_scanning functions in sequence.

import socket  #Used for checking open ports.
import subprocess # Used for running system commands.
import os #Used for running system commands

def intrusion_detection(ip_address):
    # Function to detect potential intrusions using a ping scan
    try:
        # Ping the IP address once to check if the host is up
        subprocess.check_call(['ping', '-c', '1', ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Host {ip_address} is up.")
    except subprocess.CalledProcessError:
        # If the ping fails, the host is down or unreachable
        print(f"Host {ip_address} is down or unreachable.")

def compliance_checks():
    # Function to check compliance by verifying open ports
    open_ports = []
    try:
        # Check common ports (80, 443, 22, 3306) to see if they are open
        for port in [80, 443, 22, 3306]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('localhost', port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        print("Open ports:", open_ports)
    except socket.error:
        print("Error occurred while checking ports.")

def network_scanning():
    # Function to perform a simple network scan using os.system
    try:
        print("Starting network scan...")
        # Perform a ping scan on the network range 192.168.1.0/24
        os.system("nmap -sn 192.168.1.0/24")
    except Exception as e:
        print(f"Error during network scan: {e}")

def main():
    print("1. Performing intrusion detection:")
    intrusion_detection('192.168.1.1')  # Example IP address
    
    print("\n2. Performing compliance checks:")
    compliance_checks()
    
    print("\n3. Performing network scanning:")
    network_scanning()

if __name__ == "__main__":
    main()