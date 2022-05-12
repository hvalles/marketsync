# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting Orders
for p in [544892,544888,544887]:
    utils.init()
    utils.getAnswer(utils.getUrl('pedidos/totales/'+str(p)+'?'), requests.get)

