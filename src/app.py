import sys
import streamlit as st
from api.openweather import get_climate_for_location
from pprint import pprint

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    st.title('Global Weather Web App')
    st.write('Data from OpenWeather API (https://openweathermap.org/current)')
    city = st.text_input('Enter a city:')
    if not city:
        st.stop()
    
    data_climate = get_climate_for_location(city=city)
    if not data_climate:
        st.warning(f'No data found for the city {city}')
        st.stop()
    
    current_climate = data_climate['weather'][0]['description']
    temperature = data_climate['main']['temp']
    feels_like = data_climate['main']['feels_like']
    humidity = data_climate['main']['humidity']
    clouds = data_climate['clouds']['all']
    
    st.metric(label='Current Climate', value=current_climate)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label='Temperature', value=f'{temperature}°C')
        st.metric(label='Feels Like', value=f'{feels_like}°C')
    with col2:
        st.metric(label='Humidity', value=f'{humidity}%')
        st.metric(label='Clouds', value=f'{clouds}%')
        
if __name__ == '__main__':
    main()