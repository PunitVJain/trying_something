import requests

url = "https://www.google.com/"

#  GET simple method 
response = requests.get(url)

#print(response.url)
#print(response.headers['Date'])
#print(response.text)
#print(dir(response))

# POST method
res = requests.post(url)
#print(res.url)
#print(res.headers)
print(res.text)


