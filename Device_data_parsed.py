import simplejson as json
from pprint import pprint
import csv
import re
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

username = "sysadmin"
password = "Zenoss@123"
server = "zenoss5.zenccdemo.vtslind.com"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
headers = {"content-type": "application/json"}
url = "https://%s:%s@%s/zport/dmd/device_router" % (username,password,server)
get_data = {"action":"DeviceRouter", "method":"getDevices", "data":[{}], "tid":1}
r = requests.post(url,data=json.dumps(get_data),verify=False,headers=headers)
json_data = r.content
device_data = json.loads(json_data)

csvObj = open('Device_Data.csv', 'w')
csvObj.write("IpAddress,Device Class,Production state,Collector,Systems,Locations,Groups\n")
for data_key in device_data['result']['devices']:
	data_str = str(data_key)
	print data_str
#	exit()
	location_path = ''
	groups_path = ''
	system_path = ''
	collector_location = ''	

	#Device Class
	uid = data_key['uid']
	uid = re.sub(r'\/zport\/dmd(\/.+?)\/devices(\/.+)',r'\1\2',str(uid))

	# IP Address
	ip_group = re.search(r'ipAddressString\':\s*u\'\s*(.+?)\'',data_str,re.I)
	ip_address = ip_group.group(1)

	# Production State
	prod_group = re.search(r'productionState\':\s*(\d+),',data_str,re.I)
	prod_state =  prod_group.group(1)

	#Collector
	collector_group = re.search(r'collector\':\s*u\'(.+?)\',',data_str,re.I)
	collector_location = collector_group.group(1)	

	#System Path
	if not re.search(r'systems\':\s*\[\]',data_str):
		system_group = re.search(r'systems\':.+?u\'name\':\s*u\'(.+?)\'',data_str,re.I)
		system_path = system_group.group(1)
	
	#Location Path
	if not re.search(r'location\':\s*None',data_str):
		location_group = re.search(r'location\':.+?u\'name\':\s*u\'(.+?)\'',data_str,re.I)
      		location_path = location_group.group(1)

	#Group Path
	if not re.search(r'groups\':\s*\[\]',data_str):
		groups_group = re.search(r'groups\':.+?u\'name\':\s*u\'(.+?)\'',data_str,re.I)
        	groups_path = groups_group.group(1)

	csvObj.write(ip_address+','+uid+','+prod_state+','+collector_location+''+system_path+','+location_path+','+groups_path+"\n")
csvObj.close()
exit()
