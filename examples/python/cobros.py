# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting Kits 
# utils.parameters['beforeid'] = 
# utils.parameters['afterid'] = 
utils.parameters['orders'] = "1052"
utils.getAnswer(utils.getUrl('cobros?'), requests.get) 

# utils.init()
# utils.parameters['orders'] = "1052"
# p={
#     'caja':'5',
#     'monto':'659',
#     'sucursal':'La Fe',
#     'ticket':'123456'
# }
# utils.getAnswer(utils.getUrl('cobros?'), requests.post, [p])

# utils.init()
# utils.parameters['ids'] = "4"
# p={
#     'motivo':'Cliente se arrepintio',
# }
# utils.getAnswer(utils.getUrl('cobros?'), requests.put, [p])
