""" Simple weather data from weathermap API. """
from __future__ import print_function
import requests
from ConfigParser import ConfigParser


def upcoming_forecast(api_key, lat, lon):
    """ Pulls upcoming forecast based on latitude and longitude. """
    resp = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                        params={'lat': lat, 'lon': lon, 'appid': api_key,
                                'units': 'metric'})
    return resp.json()


def get_config():
    """ Return my config object. """
    conf = ConfigParser()
    conf.read('config/prod.cfg')
    return conf

config = get_config()

print(upcoming_forecast(
    config.get('openweather', 'api_key'), 52.520645, 13.409779))
