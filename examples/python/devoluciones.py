# -*- coding: utf-8 -*-

import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Get returns betwen dates
utils.parameters['after'] = '2024-01-01T00:00'
utils.parameters['before'] = '2024-01-31T23:59'
utils.getAnswer(utils.getUrl('devoluciones?'), requests.get) 

#Update return as received
# Expected values in object
# row_id, devuelto, recibe_id, fecha, observaciones
d = {}
d['row_id'] = 89 # Identifier of detailed row
d['devuelto'] = 1 # Quantity received
d['recibe_id'] = 0 # User who receives product, can be 0
d['fecha'] = '2024-01-15T16:20:00' # When product was received format YYYY-MM-DDThh:mm:ss
d['observaciones'] = '' # Any relevant information about received items [max 500 chars]

received = [d]

# Initialize component
utils.init()
utils.getAnswer(utils.getUrl('devoluciones?'), requests.put, received) 





