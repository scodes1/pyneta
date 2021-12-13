from netmiko import ConnectHandler
from getpass import getpass

# Create device dict's
nxos1 = {
    'host':'nxos1.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_nxos',
}
nxos2 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_nxos',
}
#create a list of nxos devices
devices = [nxos1,nxos2]


#loop through nxos devices to configure 5 vlans from file.
#save config once complete
for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file(config_file='my_vlans.txt')
    print(net_connect.find_prompt())
    print(output)
    output += net_connect.save_config()
    print(output)



