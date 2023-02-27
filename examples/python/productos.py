# -*- coding: utf-8 -*-

import requests
import sys
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.


################# Recuperacion de productos
#utils.parameters['limit'] = 1
#utils.getAnswer(utils.getUrl('productos?'), requests.get)

################# Inserción de Productos
utils.init()
p={}
p['nombre'] = "Test product for API Guide"
p['descripcion'] = "This is a test for add items from API to Marketsync products"
p['ficha'] = """
Alta de la ficha t&eacute;cnica
-----------------------------------------
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
"""
p['alto'] = 12 # Centimeters height
p['ancho'] = 10 # Centimeters width
p['largo'] = 20 # Centimeters deep
p['peso'] = 1 # Kilograms deep
p['sku'] = '88963-1'
p['dias_embarque'] = 5 
p['categoria_id'] = 14833  # ACCESORIOS PARA VEHICULOS/HERRAMIENTAS/ADHESIVOS/
p['filtro_id'] = '' # Empty value
p['marca'] = "New Wave"
p['etiquetas'] = "Test,API"
p['etiquetas_web'] = "Field1_Value,Field2_Value" # Filtro field _ value for Shopify filters
p['modelo'] = "T-1000"
p['listing_type_id'] = 'gold_pro' #gold_pro, gold_special
p['warranty'] = "30 días de garantía en fabricación"
p['nombre_modelo'] = '' # Empty value
p['origen'] = 484 # México
p['color'] = "Negro Azabache" # Customer Color
p['base'] = "Negro".upper() # Must be uppercase
p['palto'] = p['alto'] # All dimensions are in centimeters
p['pancho'] = p['ancho']
p['plargo'] = p['largo']
p['ppeso'] = p['peso'] # All weights are in kilograms
# When item starts to be commercialized
p['date_created'] = '2019-01-01T00:00:00'

atributos = []
atributos.append({'atributo' : 'BRAND',           'valor' : 'New Wave'})
atributos.append({'atributo' : 'ITEM_CONDITION',  'valor' : 'Nuevo'}) # New
atributos.append({'atributo' : 'MODEL',           'valor' : 'T-1000'}) # New
atributos.append({'atributo' : 'IS_KIT',            'valor' : 'No'}) # Sí/No

p['atributos'] = atributos
items = [p]

utils.getAnswer(utils.getUrl('productos?'), requests.post, items)


sys.exit(0)

############### Actualización de Productos PUT
utils.init()

p={}
p['product_id'] = 163766 # Yous ID code
p['nombre'] = "Test product for API Guide"
p['descripcion'] = "This is a test for add items from API to Marketsync products"
p['ficha'] = """
Alta de la ficha t&eacute;cnica
-----------------------------------------
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
p['palto'] = 11 # Centimeters height
p['pancho'] = 11 # Centimeters width
p['plargo'] = 22 # Centimeters deep
p['ppeso'] = 1.2 # Kilograms weight
p['etiquetas_web'] = "Test1_Value,Test2_Value"

atributos = []
atributos.append({'atributo' : 'BRAND',           'valor' : 'New Waves'})
p['atributos'] = atributos
items = [p]

utils.getAnswer(utils.getUrl('productos?'), requests.put, items)

############### Eliminación de Productos DELETE
# utils.init()
# items = []
# items.append({'product_id':0}) # your id here

# utils.getAnswer(utils.getUrl('productos?'), requests.delete, items)