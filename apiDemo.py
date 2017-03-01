#!/usr/bin/env python


#Similar Image Search api demo
import requests
import sys
import os
import json
import base64
import argparse

clientId = "your ID here" #replace with your clientId
clientSecret = "your SECRET here" #replace with your clientSecret
mUrl = "http://goo.gl/8fgVc4" #default media to search on

ip = 'https://api.scopemedia.com'
api = "/search-service/api/v1/search/similar"

def initial_parameters():
    auth = "?client_id="+clientId+"&client_secret="+clientSecret
    url = ip + api + auth
    return url


def similar_search(s, url, search_mode, data):
    if search_mode == "remote":
        payload = {'appId': 'fashion',
                   'mediaUrl': data}
        res = s.post(url, data = json.dumps(payload))
    else:
        with open(data, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        payload = {'appId':'fashion',
                   'encodedMediaFile': encoded_string}
        res = s.post(url, data = json.dumps(payload))

    return res




if __name__ == "__main__":
    url = initial_parameters()
    #Set up requests session
    s = requests.Session()
    headers = {'Content-Type': 'application/json'}
    s.headers.update(headers)

    #Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', help='The search mode to use (e.g. local, remote', choices=['local', 'remote'], required=True)
    parser.add_argument('-r', '--remote',  help='A valid remote url of the image you want as query image', metavar='')
    parser.add_argument('-l',  '--local',  help='A local image file you want to use as query image', metavar='')
    args = parser.parse_args()
    search_mode = args.mode
    if search_mode == 'local':
        if args.local is None:
            print "please enter a local image file as query image"
        else:
            local_file = args.local
            data = local_file
            res = similar_search(s, url, search_mode, data)

            if res.status_code == 200:
                data = json.loads(res.text)
                print json.dumps(data['medias'], indent = 4)
            else:
                print res.text

    elif search_mode == 'remote':
        if args.remote is None:
            print "please enter a valid remote url as query image"
        else:
            remote_url = args.remote
            data = remote_url
            res = similar_search(s, url, search_mode, data)
            
            if res.status_code == 200:
                data = json.loads(res.text)
                print json.dumps(data['medias'], indent = 4)
            else:
                print res.text


