import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting countries
utils.getAnswer(utils.getUrl('paises?'), requests.get)

