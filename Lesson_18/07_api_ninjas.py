# https://api-ninjas.com/api
# https://api-ninjas.com/api/qrcode
import requests
import pprint
from concurrent import futures
from ninja_secrets import API_KEY

cities = ('london', 'kyiv', 'paris', 'madrid', 'oslo')
api_url_template = 'https://api.api-ninjas.com/v1/weather?city={}'


def get_city_weather(target_city):
    city_weather_data = {}
    response = requests.get(api_url_template.format(target_city), headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        city_weather_data = response.json()
    else:
        print("Error:", response.status_code, response.text)
    return city_weather_data


with futures.ThreadPoolExecutor(max_workers=4) as executor:
    futures_result = {}
    for city in cities:
        futures_result[executor.submit(get_city_weather, city)] = city
    for future in futures.as_completed(futures_result.keys()):
        print('-' * 30)
        print(f'city={futures_result[future]}')
        pprint.pprint(future.result())
