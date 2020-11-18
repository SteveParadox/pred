import json

import requests
import random


class Prediction:
    link = []
    p = range(1, 15)
    for a in p:
        url = requests.get(f'https://livescore-api.com/api-client/fixtures/matches.json?&key=ZrrUvfcMuMdveWgO&secret=UDjsfGkjTwfY7h56Ix1dNd0h0eMea335+{a}')
        link.append(url)

    def __init__(self):
        self.__link = Prediction.link

    def model(self):
        url = requests.get(
            f'https://livescore-api.com/api-client/fixtures/matches.json?&key=ZrrUvfcMuMdveWgO&secret=UDjsfGkjTwfY7h56Ix1dNd0h0eMea335')
        link= json.loads(url.text)
        link.pop('success')
        for i, e in link.items():
            v = []
            e.pop('prev_page')
            e.pop('next_page')
            for w, x in e.items():
                for o in x:
                    f = [n for i, n in o['competition'].items()]
                    v.append(o['home_name'] + ' vs ' + o['away_name'] + ' || ' + f[-1] + ' || ' + o['time'] + ' || ' + o['date'])


        pass
