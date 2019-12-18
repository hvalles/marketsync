import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Get Variacion uncomment next 2 lines for testing
#utils.parameters['ids'] = '163515'
#utils.getAnswer(utils.getUrl('variacion?'), requests.get)

utils.init()

v = {}
v['product_id'] = 163766
v['sku'] = '9815-1'
v['color'] = "Negro Noche"
v['base'] = "Negro".upper() # ;ist be upper case
v['stock'] = 0
v['imagen1'] = 'https://www.w3schools.com/w3css/img_lights.jpg'
v['imagen2'] = 'https://www.w3schools.com/w3css/img_snowtops.jpg'
v['imagen3'] = ''
v['imagen4'] = ''
v['imagen5'] = ''
v['imagen6'] = ''

v['bullet1'] = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
v['bullet2'] = 'Lorem Ipsum has been the industry s standard dummy text ever since the 1500s'
v['bullet3'] = ''
v['bullet4'] = ''
v['bullet5'] = ''

v['atributos'] = [
    {'atributo':'EAN', 'valor': '9856472536978'},
    {'atributo':'SELLER_SKU', 'valor' : '9815-1'}
]

items=[v]
utils.getAnswer(utils.getUrl('variacion?'), requests.post, items)


# PUT Variacion 

utils.init()
v = {}
v['product_id'] = 163766
v['sku'] = '9815-1'
v['color'] = "Negro Noche"
v['base'] = "Negro".upper() # ;ist be upper case
v['stock'] = 0
v['imagen1'] = 'https://www.w3schools.com/w3css/img_lights.jpg'
v['imagen2'] = 'https://www.w3schools.com/w3css/img_snowtops2.jpg'
v['imagen3'] = 'https://www.w3schools.com/w3css/img_snowtops3.jpg'
v['imagen4'] = 'https://www.w3schools.com/w3css/img_snowtops4.jpg'
v['imagen5'] = ''
v['imagen6'] = ''

v['bullet1'] = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
v['bullet2'] = 'Lorem Ipsum has been the industry s standard dummy text ever since the 1500s'
v['bullet3'] = 'Lorem Ipsum Text'
v['bullet4'] = ''
v['bullet5'] = ''

v['atributos'] = [
    {'atributo':'EAN', 'valor': '9856472536978'},
    {'atributo':'SELLER_SKU', 'valor' : '9815-1'}
]

items=[v]
utils.getAnswer(utils.getUrl('variacion?'), requests.put, items)


###### Verbo DELETE
# Delete Variacion uncomment next lines for testing

# utils.init()
# v = {}
# v['product_id'] = 163766
# v['sku'] = '9815-1'

# items=[v]
# utils.getAnswer(utils.getUrl('variacion?'), requests.delete, items)




