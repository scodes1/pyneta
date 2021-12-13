from netmiko import ConnectHandler
from getpass import getpass
 
#Create dict with details of cisco ios device
device1 = {
    'host' :'cisco1.lasthop.io',
    'username' :'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_ios',
    #'session_log' : 'my_session.txt'
}
#Create dict with details of cisco nxos device
device2 = {
    'host' :'nxos1.lasthop.io',
    'username' :'pyclass',
    'password' : getpass(),
    'device_type' : 'cisco_nxos',
    #'session_log' : 'my_session.txt'
}

#create a list with some devices in them.
devices = (device1,device2)

#loop through the list of devices
for device in devices:
    #Connect to the item in list devices
    net_connect = ConnectHandler(**device)
    #If the device is cisco IOS send collect show version and save as show_version.txt
    if device['device_type'] == 'cisco_ios':
        show_ver = net_connect.send_command("show version")
        with open("show_version.txt", "w") as f:
            f.write(show_ver)

    print(net_connect.find_prompt())


net_connect.disconnect()

