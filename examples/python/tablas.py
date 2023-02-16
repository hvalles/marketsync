import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Getting stand alone category
utils.getAnswer(utils.getUrl('tablas?'), requests.get)

# Getting attributes from a category
utils.getAnswer(utils.getUrl('tablas/detalle/117?'), requests.get)
