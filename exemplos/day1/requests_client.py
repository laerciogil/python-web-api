import requests

result = requests.get("http://example.com")
print(result.status_code)
print(result.headers)
print(result.content)
print(result.text)