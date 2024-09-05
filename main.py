import ipaddress
import pandas as pd
import csv
import io

# Use io.StringIO to simulate file reading in this environment
csv_file = 'subnets.csv'

# Reading the CSV content into a pandas DataFrame
subnets_df = pd.read_csv(csv_file)

# Extracting the subnet list from the DataFrame
subnets = subnets_df['Subnet'].tolist()

# Initialize a dictionary to hold results
subnet_ips = {}

# Process each subnet
for subnet in subnets:
    net = ipaddress.ip_network(subnet, strict=False)
    subnet_ips[subnet] = [str(ip) for ip in net.hosts()] if net.num_addresses > 1 else [str(net.network_address)]

# Convert to a DataFrame for easy display
df = pd.DataFrame(list(subnet_ips.items()), columns=["Subnet", "IP Addresses"])

# Expanding the dictionary to list one IP per line
expanded_data = []

for subnet, ips in subnet_ips.items():
    for ip in ips:
        expanded_data.append({"Subnet": subnet, "IP Address": ip})

# Convert to a DataFrame for easier display
expanded_df = pd.DataFrame(expanded_data, columns=["Subnet", "IP Address"])

# Export the expanded DataFrame as a new CSV file
expanded_csv_file_path = 'IP-Addresses.csv'

# Save the expanded DataFrame to a CSV file
expanded_df.to_csv(expanded_csv_file_path, index=False)
