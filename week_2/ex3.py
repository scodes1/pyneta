from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    'host':'cisco4.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output1 = net_connect.send_command("show version", use_textfsm=True)
output2 = net_connect.send_command("show lldp neighbors", use_textfsm=True)

print("HPE Switch Connection Port: {}".format(output2[0]["local_interface"]))
