import ipaddress
import math

def FLSM():
    print("===== FLSM Subnetting =====")
    network_input = input("Enter Network Address (EX: 192.168.1.0/24): ")
    network = ipaddress.IPv4Network(network_input, strict=False)
    num_subnets = int(input("Enter Number of Required Subnets: "))

    # Calculate borrowed bits
    borrowed_bits = math.ceil(math.log2(num_subnets))
    # New prefix length
    new_prefix = network.prefixlen + borrowed_bits
    # Generate subnets
    subnets = list(network.subnets(new_prefix=new_prefix))

    print("FLSM Subnet Details")
    print("====================")
    for i, subnet in enumerate(subnets[:num_subnets], start=1):
        hosts = list(subnet.hosts())
        
        print(f"Subnet {i}")
        print(f"Network Address   : {subnet.network_address}")
        print(f"Broadcast Address : {subnet.broadcast_address}")
        print(f"Subnet Mask       : {subnet.netmask}")
        if len(hosts) > 0:
            print(f"First Host        : {hosts[0]}")
            print(f"Last Host         : {hosts[-1]}")
            print(f"Total Hosts       : {len(hosts)}")
            print(" ")
        else:
            print("No usable hosts")

def VLSM():
    print("===== VLSM Subnetting =====")
    base_network_input = input("Enter Base Network (EX: 192.168.1.0/24): ")
    base_network = ipaddress.IPv4Network(base_network_input, strict=False)
    num_departments = int(input("Enter Number of Subnets: "))
    requirements = {}

    for i in range(num_departments):
        dept = input(f"Enter Subnet Name {i+1}: ")
        hosts = int(input(f"Enter Required Hosts for {dept}: "))
        requirements[dept] = hosts

    # Sort largest subnet first
    sorted_requirements = sorted(requirements.items(), key=lambda x: x[1], reverse=True)
    current_ip = int(base_network.network_address)

    print("VLSM Subnet Details")
    print("====================")
    for dept, hosts_needed in sorted_requirements:
        total_needed = hosts_needed + 2
        subnet_bits = math.ceil(math.log2(total_needed))
        prefix = 32 - subnet_bits
        subnet = ipaddress.IPv4Network((current_ip, prefix), strict=False)
        hosts = list(subnet.hosts())

        print(f"Subnet : {dept}")
        print(f"Required Hosts    : {hosts_needed}")
        print(f"Subnet            : {subnet}")
        print(f"Subnet Mask       : {subnet.netmask}")
        print(f"Network Address   : {subnet.network_address}")
        print(f"Broadcast Address : {subnet.broadcast_address}")
        if len(hosts) > 0:
            print(f"First Host        : {hosts[0]}")
            print(f"Last Host         : {hosts[-1]}")
            print(f"Available Hosts   : {len(hosts)}")
            print(" ")
        else:
            print("No usable hosts")
        current_ip += subnet.num_addresses

if __name__ == "__main__":
    while True:
        print("============================")
        print(" FLSM and VLSM Subnetting Tool")
        print("============================")
        print("1. Fixed Length Subnet Masking (FLSM)")
        print("2. Variable Length Subnet Masking (VLSM)")
        print("3. Exit")
        choice = input("Enter Your Choice: ")

        if choice == '1':
            FLSM()
        elif choice == '2':
            VLSM()
        elif choice == '3':
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Please Try Again.")