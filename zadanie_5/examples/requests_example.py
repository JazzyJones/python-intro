import requests

response = requests.get('https://www.example.com')
print("Status code:", response.status_code)
print("First 200 characters of content:")
print(response.text[:200])
