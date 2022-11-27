import requests


raspberry_payload = {
    "id": 1, 
    "data": {
        "sensorMetric": "temperature"
    }   
}

headers = { "Content-Type": "application/json"}


# r = requests.get("https://bed9-73-182-155-254.ngrok.io/pi/temp/", headers=headers)
# print(r.status_code)
# print(r.json())



r = requests.post("https://yiqiqjroo2.execute-api.us-east-1.amazonaws.com", json=raspberry_payload, headers=headers)
print(r.status_code)
print(r.json())