import requests

api_key='4fabc310a065dde0b3e368629ebac36f'

user_city=input('enter the city: ")
print(user_city)
weather_data= requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&units=imperial&APPID={api key}')
#weather data variable uses the request library t go and fetch the url

#print(weather_data.status_code)#attribute returns a number that indicates the status of the request
#print(weather_data.json())#deserializes the response content and returns a Python dictionary
if weather_data.json()['cod'] == '404';
print('Enter the correct city name')
else:
weather=weather_data.json()['weather'][ø]['main']
fahrenheit=weather_data.json()['main']['temp']
temp=round((fahrenheit-32)*5/9
print(f'Weather in {user_city} is {weather}')
print(f'Temparture in {user_city} is {temp}')
