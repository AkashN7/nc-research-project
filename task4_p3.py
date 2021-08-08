import requests

response = requests.get("https://holidayapi.com/")

print(response.status_code)
