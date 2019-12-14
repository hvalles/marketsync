import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Getting markets
utils.getAnswer(utils.getUrl('markets?'), requests.get)

# Posting market
utils.init()
# One market at a time
market = {'market_id':1, 'activo':1, 'proteccion':1}
utils.getAnswer(utils.getUrl('markets?'), requests.post, market)