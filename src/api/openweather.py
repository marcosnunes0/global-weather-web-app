import requests
import os
import sys
from dotenv import load_dotenv

def make_request(url, params=None):
    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Unable to make request! Error: {e}')
        resultado = None
    else:
        resultado = resposta.json()
    return resultado

def get_climate_for_location(city):
    load_dotenv()

    try:
        token = os.environ['OPENWEATHER_API_KEY']
    except KeyError:
        print("Error: Environment variable 'OPENWEATHER_API_KEY' not set. ")
        print("Please set the environment variable before running the script.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error accessing environment variables: {str(e)}")
        sys.exit(1)

    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'appid': token,
        'q': city,
        'units': 'metric',
        'lang': 'en'
    }
    
    climate_data = make_request(url=url, params=params)
    return climate_data