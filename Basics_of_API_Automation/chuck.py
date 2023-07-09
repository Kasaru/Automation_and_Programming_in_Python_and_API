import requests

url = "https://api.chucknorris.io/jokes/random"

result = requests.get(url)
result.encoding = "utf-8"
print(result.text)
assert 200 == result.status_code, "Url is incorrect"
print(f"Status code: {result.status_code}")