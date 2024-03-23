import requests

a = requests.get("http://www.gamersgift.com",proxies={"https":"129.159.225.178:33351","https":"129.159.225.178:33351"})
print(a)