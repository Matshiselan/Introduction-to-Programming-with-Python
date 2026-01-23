# Libraries
from address_processor import get_location_coordinates
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from datetime import date, timedelta


# Modular main function to run the program
def main():
    try:
        location_data = get_user_location()
        if location_data is None:
            print("Exiting the program.")
        weather_response = fetch_weather_data(location_data)
        weather_df = process_weather_data(weather_response)
        return display_weather_data(weather_df)
    except Exception as e:
        print(f"An error occurred: {e}")


# function to get location data from user input
def get_user_location():
    address = input("Enter an address (or 'exit' to quit): ")
    if address.lower() == 'exit':
        return None
    location_data = get_location_coordinates(address)
    if location_data is None:
        print(f"Location '{address}' not found. Please try again.")
        return None
    return location_data


# function to fetch weather data for a given location
def fetch_weather_data(location_data):
    latitude = location_data[0]
    longitude = location_data[1]
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)
    start_date = date.today() - timedelta(days=7)
    end_date = date.today()
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max", "temperature_2m_min", "sunshine_duration",
            "daylight_duration", "rain_sum", "snowfall_sum", "precipitation_sum"
        ],
        "timezone": "GMT",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
    }
    responses = openmeteo.weather_api(url, params=params)
    return responses[0]

# function to process weather data and return a DataFrame
def process_weather_data(response):
    daily = response.Daily()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_sunshine_duration = daily.Variables(2).ValuesAsNumpy()
    daily_daylight_duration = daily.Variables(3).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(4).ValuesAsNumpy()
    daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(6).ValuesAsNumpy()
    daily_data = {
        "date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        ),
        "temperature_2m_max": daily_temperature_2m_max,
        "temperature_2m_min": daily_temperature_2m_min,
        "sunshine_duration": daily_sunshine_duration,
        "daylight_duration": daily_daylight_duration,
        "rain_sum": daily_rain_sum,
        "snowfall_sum": daily_snowfall_sum,
        "precipitation_sum": daily_precipitation_sum,
    }
    return pd.DataFrame(data=daily_data)

# function to display the weather data DataFrame
def display_weather_data(df):
    print("\nDaily weather for the past week:\n", df)


if __name__ == "__main__":
    main()