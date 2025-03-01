import requests

def turn_on_light():
    bridge_ip = "192.168.1.100"  # Your Hue Bridge IP
    api_key = "your_api_key_here"
    light_id = 1  # The ID of the light to control

    url = f"http://{bridge_ip}/api/{api_key}/lights/{light_id}/state"
    payload = {"on": True}
    response = requests.put(url, json=payload)
    
    if response.status_code == 200:
        print("Light turned on")
    else:
        print("Failed to turn on light")
