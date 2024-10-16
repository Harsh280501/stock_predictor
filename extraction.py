import pandas as pd
import requests
import numpy as np
import datetime
import json
import http.client, urllib.parse


conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': '4eb12b615a4a20d5a13703f6d907ead2',
    'categories': '-general,-sports',
    'sort': 'published_desc',
    'limit': 10,
    })

conn.request('GET', '/v1/news?{}'.format(params))
res = conn.getresponse()
data_str = res.read()
data_json = json.loads(data_str)
print(data_json)


author = data_json['data'][0]['author']
print(author)
