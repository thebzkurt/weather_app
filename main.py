import  requests
from Tools.scripts.pathfix import preserve_timestamps

#Step 1: API SETUP
API_KEY = "a19949006367bbf29bc47a3d432bf3ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#Step 2: Get weather data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data['name'],
                "Temperature": f"{data['main']['temp']}C",
                "Weather": f"{data['weather'][0]['description'].title()}",
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']}m/s"
            }
            return weather
        elif response.status_code == 404:
            print("City not found")
        else:
            print("An error occurred, Status code", response.status_code)
    except Exception as e:
        print("An error occurred: ", e)
        return None

#Step 3: Display weather information
def display_weather(weather):
    print("\n---- Weather Information ----")
    for key, value in weather.items():
        print(f"{key}: {value}")

#Step 4: Mein loop

while True:
    print("\n---- Weather App ----")
    city = input("Enter a city name or quit for press 'q': ").strip()
    if city.lower() == 'q':
        break
    weather = get_weather(city)
    if weather:
        display_weather(weather)
