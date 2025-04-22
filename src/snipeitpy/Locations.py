import requests
import urllib3
import json


class Locations(object):

    def __init__(self, url, token, limit=None, order='asc', offset=None):
        self.url = url
        self.token = token
        self.limit = None
        self.order = 'asc'
        self.offset = None

        self.headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _getLocations(self):
        if self.limit is not None:
            self.uri = f'/api/v1/locations?limit={self.limit}&order={self.order}'
        else:
            self.uri = f'/api/v1/locations?order={self.order}'

        if self.offset is not None:
            self. uri = f'{self.url}{self.uri}&offset={self.offset}'

        self.url = f'{self.url}{self.uri}'
        
        locations = requests.get(self.url, headers=self.headers, verify=False)
        
        return locations.content

    def _getLocationById(self, location_id):
        self.uri = f'/api/v1/locations/{location_id}'
        
        self.url = f'{self.url}{self.uri}'
        
        location = requests.get(self.url, headers=self.headers, verify=False)

        return location.content


