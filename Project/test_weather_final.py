import pytest
from unittest.mock import patch, MagicMock
from weather_final import WeatherFetcher

@pytest.fixture
def weather_fetcher():
    return WeatherFetcher()

def test_process_weather_data_returns_dataframe(weather_fetcher):
    # Mock the response object with the necessary methods/attributes
    mock_daily = MagicMock()
    mock_daily.Time.return_value = 1705968000  # Example timestamp
    mock_daily.TimeEnd.return_value = 1706572800
    mock_daily.Interval.return_value = 86400
    # 7 days of data
    mock_daily.Variables.side_effect = lambda i: MagicMock(ValuesAsNumpy=MagicMock(return_value=[1,2,3,4,5,6,7]))
    mock_response = MagicMock()
    mock_response.Daily.return_value = mock_daily

    df = weather_fetcher.process_weather_data(mock_response)
    assert not df.empty
    assert list(df.columns) == [
        'date', 'temp_max', 'temp_min', 'sunshine', 'daylight', 'rain', 'snow', 'precipitation'
    ]
    assert len(df) == 7

@patch('weather_final.get_location_coordinates')
def test_get_user_location_valid(mock_get_loc, weather_fetcher):
    mock_get_loc.return_value = (1.0, 2.0)
    with patch('builtins.input', return_value='Harare'):
        loc = weather_fetcher.get_user_location()
        assert loc == (1.0, 2.0)

@patch('weather_final.get_location_coordinates')
def test_get_user_location_invalid(mock_get_loc, weather_fetcher):
    mock_get_loc.return_value = None
    with patch('builtins.input', return_value='NowhereLand'):
        loc = weather_fetcher.get_user_location()
        assert loc is None

@patch('weather_final.get_location_coordinates')
def test_get_user_location_exit(mock_get_loc, weather_fetcher):
    with patch('builtins.input', return_value='exit'):
        loc = weather_fetcher.get_user_location()
        assert loc is None
