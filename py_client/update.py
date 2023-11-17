import requests

endpoint = "http://localhost:8000/api/products/3/update/"

data = {
    "title" : "Hello Django My old View again!",
    "price" : 233.87
}

get_response = requests.put(endpoint, json=data)

print(get_response.json())

