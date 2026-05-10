from urllib.request import urlopen

url = "http://example.com"
response = urlopen(url)
print(response)
print(response.read())
