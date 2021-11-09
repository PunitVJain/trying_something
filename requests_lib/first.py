import requests

url = "https://www.google.com/"


response = requests.get(url)

#print(response.url)
#print(response.headers)
print(response.text)
