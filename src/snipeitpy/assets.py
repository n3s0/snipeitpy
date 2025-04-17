import requests
import urllib3
import json


class Assets(object):

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

    def _getAssets(self):
        if self.limit is not None:
            self.uri = f'/api/v1/hardware?limit={self.limit}&order={self.order}'
        else:
            self.uri = f'/api/v1/hardware?order={self.order}'

        if self.offset is not None:
            self. uri = f'{self.url}{self.uri}&offset={self.offset}'

        self.url = f'{self.url}{self.uri}'
        
        assets = requests.get(self.url, headers=self.headers, verify=False)
        
        return assets.content

    def _getAssetsById(self, asset_id):
        self.uri = f'/api/v1/hardware/{asset_id}'
        
        self.url = f'{self.url}{self.uri}'
        
        asset = requests.get(self.url, headers=self.headers)

        return asset.content

    def _getAssetsByTag(self, asset_tag):
        self.uri = f'/api/v1/hardware/{asset_tag}'
        
        self.url = f'{self.url}{self.uri}'
        
        asset = requests.get(self.url, headers=self.headers)

        return asset.content

    def _getAssetsBySerial(self, sn):
        self.uri = f'/api/v1/hardware/{sn}'
        
        self.url = f'{self.url}{self.uri}'
        
        asset = requests.get(self.url, headers=self.headers)

        return asset.content

