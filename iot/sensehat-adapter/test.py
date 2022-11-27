import requests


raspberry_payload = {
    "id": 1, 
    "data": {
        "sensorMetric": "temperature"
    }   
}


pi_temp_payload = {
    "id": 1, 
    "data": {
        "sensorMetric": "pressure"
    }   
}

headers = { "Content-Type": "application/json"}


# r = requests.get("https://bed9-73-182-155-254.ngrok.io/pi/temp/", headers=headers)
# print(r.status_code)
# print(r.json())


# Sense Hat Lambda
r = requests.post("https://5bqtjwld9f.execute-api.us-east-1.amazonaws.com", json=raspberry_payload)
print(r.status_code)
print(r.json())


# r = requests.post("https://1om6em92sb.execute-api.us-east-1.amazonaws.com", json=raspberry_payload, headers=headers)
# print(r.status_code)
# print(r.json())