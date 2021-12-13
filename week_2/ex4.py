from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    'host':'cisco3.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios'
}

net_connect = ConnectHandler(**device1)

cfg = [
    'ip name-server 1.1.1.1',
    'ip name-server 1.0.0.1',
    'ip domain-lookup'
]

config_change = net_connect.send_config_set(cfg)
print("-"*25)
print("Sending configuration to device: ")
print("-"*25)
print('\n')
print(config_change)
print('\n')
print("-"*25)
print('\n')



verify = net_connect.send_command("ping google.com")

print('-'*25)
print('Testing DNS')
print('-'*25)
print('\n')
if '!!' in verify:
    print("DNS confirmed working")
    print(verify)
else:
    print("DNS response failed")

net_connect.disconnect()
