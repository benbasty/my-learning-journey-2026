# find longitude and latitude

import requests
city_name = 'San Francisco'
state_code = 'CA'
country_code = 'US'
API_key = '38fd8b6638b87cd6d30242b0003bae9b'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}')
print(response.text)