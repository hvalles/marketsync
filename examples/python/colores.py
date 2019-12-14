import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


# Getting colors
utils.getAnswer(utils.getUrl('colores?'), requests.get)

