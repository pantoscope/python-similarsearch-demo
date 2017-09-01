# ScopeMedia Python Demo - Similar Image Search
# URL: https://github.com/ScopeMediaInc/python-similarsearch-demo
# Docs: https://developer.scopemedia.com/documentation
import requests
import sys
import os
import json
import base64
import argparse

# Authentication
# Below clientId and clientSecret is for demo purpose
# The demo image set has 200 fashion images
# To use your image set, replace clientId and clientSecret with your client ID and secret from dashboard
clientId = 'ukKxYOZL94oDmIiPOO5GfREQHLglY25gkttmhFurUmmHSNSW1srrIY0ErT6lB3Eo'
clientSecret = 'eWq0bU8j80R5b96YZmqfWNIYVugMj89m4P79qSKl4FyYiLMBQ23TuHf56gF9RrWh'

API_URL = 'https://api.scopemedia.com/search/v2/similar'

def similar_search(payload):
    response = requestSession.post(API_URL, json.dumps(payload))

    if response.status_code == 200:
        data = json.loads(response.text)
        print json.dumps(data['medias'], indent = 4)
    else:
        print response.text

if __name__ == '__main__':
    #Set up requests session and it's headers
    requestSession = requests.Session()
    headers = {
        'Content-Type': 'application/json',
        'Client-Id': clientId,
        'Client-Secret': clientSecret
    }
    requestSession.headers.update(headers)

    #Set up argument parser
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-u', '--url',  help = 'URL of the image for searching similar image', metavar = '')
    group.add_argument('-f',  '--file',  help = 'File path of the image for searching similar image. It will be converted and included in API request as base64 string', metavar = '')
    args = parser.parse_args()
    if args.file:
        # convert image to base64 string
        with open(args.file, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
        similar_search({'base64': encoded_string})
    elif args.url:
        similar_search({'mediaUrl': args.url})
