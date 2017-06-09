import csv
import re

f1 = open('sort_ssh.csv', 'w')
f2 = open('sort_winrm.csv', 'w')
f3 = open('sort_snmp.csv', 'w')
f4 = open('sort_network.csv', 'w')
f5 = open('Device_Data.csv', 'rb')
reader = csv.reader(f5)
f1.write("IpAddress,Device Class\n")
f2.write("IpAddress,Device Class\n")
f3.write("IpAddress,Device Class\n")
f4.write("IpAddress,Device Class\n")

for row in reader:
	if re.search(r'Microsoft\/Windows',str(row[2])):
		ip_address = str(row[0])
		device_class = str(row[2])
		f2.write(ip_address+','+device_class+"\n")
	elif re.search(r'Server\/SSH\/Linux',str(row[2])):
		ip_address = str(row[0])
                device_class = str(row[2])
                f1.write(ip_address+','+device_class+"\n")
	elif re.search(r'Server\/Linux',str(row[2])):
		ip_address = str(row[0])
                device_class = str(row[2])
                f3.write(ip_address+','+device_class+"\n")
	elif re.search(r'Devices\/Network',str(row[2])):
		ip_address = str(row[0])
                device_class = str(row[2])
                f4.write(ip_address+','+device_class+"\n")

f1.close()
f2.close()
f3.close()
f4.close()
exit
