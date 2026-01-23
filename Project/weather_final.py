from datetime import date, timedelta
import pandas as pd
import openmeteo_requests
import requests_cache
from retry_requests import retry
from address_processor import get_location_coordinates

class WeatherFetcher:
    def __init__(self):
        # Initialize the API client once when the object is created
        self.cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
        self.openmeteo = openmeteo_requests.Client(session=self.retry_session)
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_user_location(self):
        address = input("Enter an address (or 'exit' to quit): ")
        if address.lower() == 'exit':
            return None
        
        location_data = get_location_coordinates(address)
        if location_data is None:
            print(f"Location '{address}' not found. Please try again.")
            return None
        return location_data

    def fetch_weather_data(self, latitude, longitude):
        # Using 2026 dates
        start_date = date.today() - timedelta(days=7)
        end_date = date.today()
        
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
        responses = self.openmeteo.weather_api(self.url, params=params)
        return responses[0]

    def process_weather_data(self, response):
        daily = response.Daily()
        daily_data = {
            "date": pd.date_range(
                start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=daily.Interval()),
                inclusive="left"
            ),
            "temp_max": daily.Variables(0).ValuesAsNumpy(),
            "temp_min": daily.Variables(1).ValuesAsNumpy(),
            "sunshine": daily.Variables(2).ValuesAsNumpy(),
            "daylight": daily.Variables(3).ValuesAsNumpy(),
            "rain": daily.Variables(4).ValuesAsNumpy(),
            "snow": daily.Variables(5).ValuesAsNumpy(),
            "precipitation": daily.Variables(6).ValuesAsNumpy(),
        }
        return pd.DataFrame(data=daily_data)

    def run(self):
        """Main execution flow inside the class"""
        try:
            location = self.get_user_location()
            if not location:
                return

            # Unpack coordinates from location_data tuple/list
            lat, lon = location[0], location[1]
            
            response = self.fetch_weather_data(lat, lon)
            df = self.process_weather_data(response)
            
            print(f"\nDaily weather for the past week (ending {date.today()}):")
            print(df)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create an instance of the class and run it
    app = WeatherFetcher()
    app.run()
