import urllib
from datetime import datetime, timedelta
import hashlib
from hmac import HMAC
import json
import requests
import config

parameters = {}

def init():
    global parameters
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
    if data:
        print json.dumps(data)
        r = accion(url, data=json.dumps(data))
    else:
        r = accion(url)

    print "--------------------------------"
    try:
        print r.json()
    except:
        print r.text

# Initialize Prameters
init()
