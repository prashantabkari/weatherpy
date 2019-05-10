import json
from  botocore.vendored import requests
import sys
 

def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(location, api_key)
    r = requests.get(url)
    return r.json()


def lambda_handler(event, context):
   
    location = 'Melbourne'
 
    api_key = "$"
    weather = get_weather(api_key, location)
 
    print(weather['main']['temp'])
    print(weather)
    
    return {
        'statusCode': 200,
        'body': json.dumps(weather['main']['temp'])
    }

