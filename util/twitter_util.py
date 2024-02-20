import requests

from config.config import appConfig


def pull_tweets(screenname):
    url = appConfig.get('rapidapi').get('url')

    querystring = {"screenname": screenname}

    headers = {
        "X-RapidAPI-Key": appConfig.get('rapidapi').get('key'),
        "X-RapidAPI-Host": appConfig.get('rapidapi').get('host')
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()
