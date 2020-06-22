# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


################# Recuperacion de productos
utils.parameters['limit'] = 3
utils.getAnswer(utils.getUrl('fulfillment?'), requests.get)
