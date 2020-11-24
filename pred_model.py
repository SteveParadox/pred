import json

import requests
import random


class Prediction:
    link = []
    x = []
    v = []
    p = range(1, 15)
    for a in p:
        url = requests.get(
            f'https://livescore-api.com/api-client/fixtures/matches.json?&key=ZrrUvfcMuMdveWgO&secret'
            f'=UDjsfGkjTwfY7h56Ix1dNd0h0eMea335+{a}')
        link.append(url.text)

    def __init__(self):
        self.__link = Prediction.link
        self.__x = Prediction.x
        self.__v = Prediction.v

    def model(self):
        for nr, url in enumerate(self.__link):
            game = json.loads(url)
            game.pop('success')
            self.__x.append(game)

            for i in self.__x:
                o = i['data']
                d = o['fixtures']

                for p in d:
                    f = [n for e, n in p['competition'].items()]
                    games = p['home_name'] + ' vs ' + p['away_name'] + ' || ' + f[-1] + ' || ' + p['time'] + ' || ' + p[
                        'date']

                    self.__v.append(games)
                    random.shuffle(self.__v)
        data = random.sample(self.__v, 100)

        random.shuffle(data)
        choice = random.sample(data, 12)
        l = []
        for a in choice:
            l.append(a)
        with open('results.txt', 'w', encoding="utf-8") as r:
            for i in l:
                r.write(i + '\n')


c = Prediction()

print(c.model())