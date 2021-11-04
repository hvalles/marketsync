# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting Kits 
# utils.parameters['beforeid'] = 
# utils.parameters['afterid'] = 
utils.parameters['ids'] = "5999"
utils.getAnswer(utils.getUrl('kits?'), requests.get) 

utils.init()
p=[]
componentes=[]
componentes.append({"sku":'12345698','cantidad':1})

p.append({'sku':'123456','comentario':'Prueba de post',"componentes":componentes})
utils.getAnswer(utils.getUrl('kits?'), requests.post, p)
