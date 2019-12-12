import urllib
from datetime import datetime, timedelta
import hashlib
from hmac import HMAC
import json
import requests
import config


# Get users test
parameters = {}
parameters['token'] = config.TOKEN
parameters['timestamp'] = str(datetime.now().isoformat())
parameters['version'] = '1.0'

def Signature(concatenated):  
    sign = HMAC(config.PRIVATE_KEY, concatenated, hashlib.sha256).hexdigest()
    return sign

def getUrl(url):
    concatenated = str(urllib.urlencode(sorted(parameters.items())))
    return config.SERVER + url + concatenated + '&signature=' + Signature(concatenated)

def getAnswer(url, accion, data=None):
    print url
    print json.dumps(data)
    if data:
        r = accion(url, data=json.dumps(data))
    else:
        r = accion(url)
    try:
        for x in r.json().get('answer',[]):
            if x.get('result', None):
                print x.get('result', None) 
            else:
                print x
            print "-----------------"
    except:
        print r.text
