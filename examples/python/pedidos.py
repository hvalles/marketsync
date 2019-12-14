import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting countries
utils.parameters['limit'] = 2
utils.getAnswer(utils.getUrl('pedidos?'), requests.get)

