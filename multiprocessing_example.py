from __future__ import unicode_literals, print_function

import requests
from multiprocessing import Pool
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

import logging


def get_config():
    """ Return my config object. """
    conf = ConfigParser()
    conf.read('config/prod.cfg')
    return conf

def get_lat_long(config, address):
    """ Returns lat and long from Google geocode API based on address. """
    qs_dict = {'address': quote_plus(address),
               'key': config.get('google', 'api_key'),
    }
    logging.debug('Requesting weather data from google for %s', address)
    resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json',
                        params=qs_dict)
    try:
        lat, lon = resp.json().get('results')[0].get('geometry').get(
                                                    'location').values()
    except KeyError:
        raise Exception('Could not find address: %s', address)
    return lat, lon

def upcoming_forecast(args):
    """ Pulls upcoming forecast based on address. """
    config, address = args
    lat, lon = get_lat_long(config, address)
    logging.debug('Have lat and long for %s', address)
    resp = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                        params={'lat': lat, 'lon': lon,
                                'appid': config.get('openweather', 'api_key'),
                                'units': 'metric'})
    return (address, resp.json())

def get_city_forecasts(addresses):
    """ Returns forecasts when given a list of string addresses based on
        Google geocoding and openweather data. """
    config = get_config()
    pool = Pool(processes=2)
    return pool.map(upcoming_forecast, [(config, addy) for
                                         addy in addresses])

my_weather = get_city_forecasts(['Los Angeles, CA', 'New York, NY',
                                 'Berlin, Germany'])

print(type(my_weather))

for item in my_weather:
    print(item[0])
