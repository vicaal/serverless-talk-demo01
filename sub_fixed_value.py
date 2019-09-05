import json
import os

def handler(event, context):
    request = json.loads(event['body'])
    
    return {
        "statusCode": 200,
        "body": "{} - {} = {}".format(int(request['val1']), int(os.environ['FIXED_VALUE']), int(request['val1']) - int(os.environ['FIXED_VALUE']))
    }