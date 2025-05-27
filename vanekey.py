import json 
from hashlib import md5
from sqlite3 import Timestamp
from requests import get
from datetime import datetime 
class RestMarvel:
    Timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')    
    pub_key = '118342875c15380dbe69675b838e2639'
    priv_key = '792adc9e4a7cbcd93610dc37e9d3f6f13b4ade51'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.Timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts': self.Timestamp, 'apikey': self.pub_key, 'hash': self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        if results.status_code == 200:
           data = results.json()
           print(data)
        else:
            print(f"Error: {results.status_code} - {results.text}")
    
rm = RestMarvel()
rm.get_heroes()
     