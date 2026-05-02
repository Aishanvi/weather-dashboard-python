import requests

api_key = "7ba2226d1cb7e8e61b184325c748ad03"

city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url, timeout=10)
try:
    data = response.json()
    if response.status_code != 200:
        print("Error:", data["message"])
        exit()
except requests.exceptions.RequestException:
    print("Unable to connect to weather service.")
    exit()
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]
print("\nWeather Details:")
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Condition:", weather)