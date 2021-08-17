import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.
import sys

# Verbo GET
utils.init()
utils.getAnswer(utils.getUrl('ubicado?'), requests.get)

# Verbo POST 
items = []
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0010', 'stock':1})
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0020', 'stock':2}) 
items.append({'ubicacion':'INC-002', 'seller_sku':'0697-1000-0010', 'stock':4})
items.append({'ubicacion':'INC-002', 'seller_sku':'0697-1000-0020', 'stock':5})
items.append({'ubicacion':'INC-003', 'seller_sku':'0697-1000-0025', 'stock':6})

utils.getAnswer(utils.getUrl('ubicado?'), requests.post, items)

# Verbo DELETE  
items = []
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0010'})
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0020'}) 
utils.getAnswer(utils.getUrl('ubicado?'), requests.delete, items)