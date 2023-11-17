import requests

headers = {
    "Authorization" : "Vishango 8579be0eeb35162bc9590877eedefaceeecd4a76"
}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"This field is token authentication!",
    "price":69.69
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

