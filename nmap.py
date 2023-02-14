import nmap

# Create an nmap scanner object
scanner = nmap.PortScanner()

# Scan the network for devices
scanner.scan(hosts='192.168.1.0/24', arguments='-sn')

# Get a list of all hosts on the network
hosts_list = list(scanner.all_hosts())

# Print the list of hosts
print(f'Number of hosts: {len(hosts_list)}')
for host in hosts_list:
    print(host)
