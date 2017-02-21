#Similar Image Search api demo
import requests
import sys
import os
import json
import base64

clientId = "your id here" #replace with your clientId
clientSecret = "your secret here" #replace with your clientSecret
mUrl = "http://goo.gl/8fgVc4" #default media to search on

ip = 'http://api.scopemedia.com'
api = "/search-service/api/v1/search/similar"

def initial_parameters():
    auth = "?client_id="+clientId+"&client_secret="+clientSecret
    url = ip+api+auth
    return url

if __name__ == "__main__":
    url = initial_parameters()
    if len(sys.argv) > 1 and len(sys.argv) == 3:
        img_url = sys.argv[1]
        search_mode = sys.argv[2]

        if search_mode == "url": #search similar: URL
            payload = {"mediaUrl": img_url}
            header = {'Content-Type': 'application/json'}
            s = requests.Session()
            s.headers.update(header)
            r = s.post(url, data=json.dumps(payload))
            print r
            if str(r) == '<Response [200]>':
                data = json.loads(r.text)
                print data['medias']
            else:
                print r.text

        else:
            if search_mode == "local_image": #search similar: local image file, base64
                with open(img_url, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read())
            elif search_mode == "remote_image": #search similar: remote image file, base64
                encoded_string = base64.b64encode(requests.get(img_url).content)
            else:
                print "Use arguments: image_url, search_mode=[url, local_image, remote_image]"

            payload = {"encodedMediaFile": encoded_string}
            header = {'Content-Type': 'application/json'}
            s = requests.Session()
            s.headers.update(header)
            r = s.post(url, data=json.dumps(payload))
            print r
            if str(r) == '<Response [200]>':
                data = json.loads(r.text)
                print data['medias']
            else:
                print r.text

    else:
        print "Use arguments: image_url, search_mode=[url, local_image, remote_image]"

