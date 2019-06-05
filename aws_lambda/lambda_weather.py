import json
import boto3
from  botocore.vendored import requests
import sys


def get_weather(api_key, location):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=metric".format(location, api_key)
    r = requests.get(url)
    return r.json()

def get_secret():
    secret_name = "weatherapi"
    region_name = "us-east-1"
    
   
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    
    if 'SecretString' in get_secret_value_response:
        secret = json.loads(get_secret_value_response['SecretString'])
    else:
        binary_secret_data = get_secret_value_response['SecretBinary']
        
    key = secret['key']
    
    return key
    
def lambda_handler(event, context):
   
    location = 'Melbourne'
    api_key = get_secret()
            
    weather = get_weather(api_key, location)
 
    print(weather['main']['temp'])
    print(weather)
    
    return {
        'statusCode': 200,
        'body': json.dumps(weather['main']['temp'])
    }
    
    
    
    
