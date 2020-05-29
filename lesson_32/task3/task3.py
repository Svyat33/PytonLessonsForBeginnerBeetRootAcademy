# Task 3
#
# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your choice.
# For the current task, you can choose any weather API or website or use https://openweathermap.org

# open weather map lib
import pyowm
import configparser

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def weather(api_key, place_input):
    ow = pyowm.OWM(api_key)
    place = ow.weather_at_place(place_input)  # obseration
    w = place.get_weather()  # get request with place
    temperature = w.get_temperature("celsius")
    status = w.get_status()
    icon = w.get_weather_icon_url()
    humidity = w.get_humidity()
    wind = w.get_wind()["speed"]  # default meters per second
    return {
        "place": place_input,
        "temperature": temperature["temp"],
        "status": status,
        "icon": icon,
        "humidity": humidity,
        "wind": wind,
    }


if __name__ == "__main__":
    api_key = get_api_key()
    place = input(f"Enter the place:\t")
    rez = weather(api_key, place)
    print(
        "Weather in {place} city | "
        "Temperature C: {temperature}\N{DEGREE SIGN} |"
        " Status: {status} {icon} \nHumidity: {humidity}\n Wind: {wind}".format(**rez)
    )
