# -*- coding: utf-8 -*-

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
    print (url)
    print (data)
    if data:
        #print json.dumps(data)
        if type(data) is dict:
            r = accion(url, data=data)
        else:
            r = accion(url, json=data)
    else:
        r = accion(url)

    print "******************************************"
    try:
        print (r.text)
    except:
        print  (''.join([i if ord(i) < 128 else ' ' for i in r.text]))

# Initialize Prameters
init()
