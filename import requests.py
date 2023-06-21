import requests
url= "https://country-leaders.onrender.com/status"
data_requests=requests.get(url)
print(data_requests.status_code)
if data_requests.status_code==200:
   print(data_requests.text)
else:
  print(data_requests.status_code) 


countries_url="https://country-leaders.onrender.com/countries"
req=requests.get(countries_url)
print(req.status_code)
print(req.json)

cookie_url="https://country-leaders.onrender.com/cookie"
cookie=requests.get(cookie_url)
print(cookie.status_code)
print(cookie.json)

leaders_url="https://country-leaders.onrender.com/leaders"
leaders=requests.get(leaders_url)
print(leaders.status_code)
print(leaders.json)