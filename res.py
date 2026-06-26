import requests
url="http://172.20.10.4:8000/update_age"
response=requests.put(url)
print(response.json())  