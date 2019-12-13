import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Put Publicar

items = []
items.append({'product_id':162699, 'market_id':1}) # Claro
items.append({'product_id':162699, 'market_id':2}) # Linio
items.append({'product_id':162699, 'market_id':4}) # MeLi
items.append({'product_id':162699, 'market_id':5}) # Walmart
items.append({'product_id':162699, 'market_id':6}) # Amazon


utils.getAnswer(utils.getUrl('productos/agotar?'), requests.put, data=items)

