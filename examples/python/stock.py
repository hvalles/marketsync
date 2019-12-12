import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

items = []
# Los markets pueden variar consulte la lista de markets disponibles en 
# /api/markets
items.append({'product_id':162700, 'seller_sku':'7811X', 'stock':1})
items.append({'product_id':162700, 'seller_sku':'7911X', 'stock':2}) 
items.append({'product_id':162700, 'seller_sku':'8011X', 'stock':4})
items.append({'product_id':162700, 'seller_sku':'8111X', 'stock':5})
items.append({'product_id':162700, 'seller_sku':'1182X', 'stock':6})

utils.getAnswer(utils.getUrl('stock?'), requests.put, items)