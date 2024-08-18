import requests

url = "http://localhost:8000/view_request_info"
headers = {
    "apiKey": "this_is_my_key"
}

response = requests.get(url, headers=headers)
print(response.json())