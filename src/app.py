import sys
from api.openweather import get_climate_for_location
from pprint import pprint

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    city = 'São Paulo' # Example city
    response = get_climate_for_location(city)
    pprint(response)
    
if __name__ == '__main__':
    main()