import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Getting stand alone category
utils.parameters['ids'] = 7209 # remover this parameter to get all categories
utils.getAnswer(utils.getUrl('categorias?'), requests.get)

# Getting attributes from a category
utils.getAnswer(utils.getUrl('categorias/atributos/7416?'), requests.get)
