import requests
import json 

url = "http://api.myip.com"
headers = {"User-agent":"Mozilla"}

req = requests.get(url,headers=headers)
resp = req.text
data = json.loads(resp)

print("[+] Ip",data['ip'])
print("[+] Country",data['country'])
