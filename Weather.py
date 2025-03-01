import requests

def get_weather(city_name):
    api_key = "your_api_key_here"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        temperature = main["temp"]
        weather_desc = data["weather"][0]["description"]
        
        print(f"Weather in {city_name}: {weather_desc}")
        print(f"Temperature: {temperature}°C")
    else:
        print("City not found!")
