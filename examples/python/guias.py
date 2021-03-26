# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting Tracking Numbers
utils.parameters['orders'] = '131303'
# utils.parameters['beforeid'] = 
# utils.parameters['afterid'] = 
# Genera la guia y la descarga, solamente una guia a la vez
utils.getAnswer(utils.getUrl('guias?'), requests.post) 

# El get funciona para multiples guias pero solamente las descarga ya deben de existir
#utils.getAnswer(utils.getUrl('guias?'), requests.get)
