# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting Tracking Numbers
utils.parameters['orders'] = '30546'
# utils.parameters['beforeid'] = 
# utils.parameters['afterid'] = 
utils.getAnswer(utils.getUrl('guias?'), requests.get)
