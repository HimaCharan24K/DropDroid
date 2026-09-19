import requests

response = requests.get(
    "https://api.telegram.org"
)

print(response.status_code)
