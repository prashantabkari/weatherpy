import logging

from flask import Flask
import json
import requests


app = Flask(__name__)


def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(location, api_key)
    r = requests.get(url)
    return r.json()


@app.route('/')
def get_weather_details():
    location = 'Melbourne'
    api_key = ''

    weather = get_weather(api_key, location)

    print(weather['main']['temp'])
    print(weather)

    return json.dumps(weather['main']['temp'])


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
