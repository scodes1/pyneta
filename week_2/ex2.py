from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

device1 = {
    'host':'nxos2.lasthop.io',
    'username':'pyclass',
    'password':getpass(),
    'device_type':'cisco_nxos',
    'global_delay_factor':2,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output1 = net_connect.send_command("show lldp neighbors detail")
print(output1)
cmd1_runtime = datetime.now()

output2 = net_connect.send_command("show lldp neighbors detail", delay_factor=8)
print(output2)
cmd2_runtime = datetime.now()

net_connect.disconnect()

print('-'*25)
print("Command1 runtime: {}".format(cmd1_runtime))
print('-'*25)
print("Command2 runtime: {}".format(cmd2_runtime))
print('-'*25)

