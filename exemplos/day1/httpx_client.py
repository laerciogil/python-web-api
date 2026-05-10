import httpx

# a comunidade python está aos poucos migrando do requests para o httpx
# o httpx é mais moderno e tem mais recursos como suporte a HTTP/2, websockets
# e chamadas assíncronas

result = httpx.get("http://example.com")
print(result.status_code)
print(result.headers)
print(result.content)
print(result.text)