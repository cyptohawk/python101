import requests

url = "http://api.myip.com"
headers = {"User-agent":"Mozilla"}

req = requests.get(url,headers=headers)
resp = req.read()
