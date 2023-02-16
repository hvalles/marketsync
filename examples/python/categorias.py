import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Getting stand alone category
utils.parameters['ids'] = 14830 # remover this parameter to get all categories
utils.getAnswer(utils.getUrl('categorias?'), requests.get)

# Getting attributes from a category
utils.getAnswer(utils.getUrl('categorias/atributos/14830?'), requests.get)
