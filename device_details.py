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
#print device_data

csvObj = open('Device_Data.csv', 'w')
csvObj.write("IpAddress,Device Name,Device Class,Production state,Collector,Systems,Locations,Groups\n")

for result in device_data['result']['devices']:
	result_str = str(result)
	location_name = ''
	group_name = ''
	system_name = ''

	#IPADDRESS
	ip_address = str(result['ipAddressString'])

	#DEVICE NAME
        device_name = str(result['name'])

	#DEVICE CLASS
	device_class = result['uid'] 
	device_class = re.sub(r'\/zport\/dmd(\/.+?)\/devices\/.+',r'\1',str(device_class))

	#PRODUCTION STATE
        prod_state = str(result['productionState'])

        #COLLECTOR
        collector_location = result['collector']
	
	#System Path
	try:
		for system in result['systems']:
			for name in system:
				system_name = system['name']
	except Exception as e:
		pass

	#Group Path
	try:
        	for group in result['groups']:
                	for name in group:
                        	group_name = group['name']
	except Exception as e:
		pass
	
	#Location Path
	try:
		location_name = result['location']['name']
	except Exception as e:
		pass

	csvObj.write(ip_address+','+device_name+','+device_class+','+prod_state+','+collector_location+','+system_name+','+location_name+','+group_name+"\n")

csvObj.close()
exit()
