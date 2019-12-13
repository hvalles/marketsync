import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Recuperacion de productos
utils.parameters['limit'] = 1
utils.getAnswer(utils.getUrl('productos?'), requests.get)

# Inserción de Productos
