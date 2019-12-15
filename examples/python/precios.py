import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


items = []
# Los markets pueden variar consulte la lista de markets disponibles en /api/markets
items.append({'product_id':163766, 'market_id':1, 'oferta':101, 'precio':201}) # Claro
items.append({'product_id':163766, 'market_id':2, 'oferta':102, 'precio':202}) # Linio
items.append({'product_id':163766, 'market_id':4, 'oferta':104, 'precio':204}) # MeLi
items.append({'product_id':163766, 'market_id':5, 'oferta':105, 'precio':205}) # Walmart
items.append({'product_id':163766, 'market_id':6, 'oferta':106, 'precio':206}) # Amazon

utils.getAnswer(utils.getUrl('precios?'), requests.put, items)