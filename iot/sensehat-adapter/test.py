import requests


raspberry_payload = {
    "id": 1, 
    "data": {
        "pi_temp": "cpuTemp"
    }   
}

headers = { "Content-Type": "application/json"}


r = requests.get("https://bed9-73-182-155-254.ngrok.io/pi/temp/", headers=headers)
print(r.status_code)
print(r.json())