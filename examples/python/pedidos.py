import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Getting countries
utils.parameters['limit'] = 2
utils.getAnswer(utils.getUrl('pedidos?'), requests.get)

# Posting new SalesOrders
utils.init()

p={}
p['referencia']='123456'
p['fecha_pedido'] = '2019-12-01T10:00:00'
p['fecha_autoriza'] = '2019-12-01T10:35:10'
p['subtotal'] = '1000'
p['total'] = '1160'
p['email'] = 'myself@mysite.com'
p['entregara'] = 'MySelf'
p['telefono'] = ''
p['direccion'] = 'Priv Reforma # 108'
p['entrecalles'] = 'Abasolo y Montero'
p['colonia'] = 'Los Treviño'
p['ciudad'] = 'Santa Catarina'
p['estado'] = 'Nuevo León'
p['observaciones'] = 'Bodega Blanca'
p['cp'] = '61588'
p['estatus'] = 'pendiente'
p['mensajeria'] = ''
p['guias'] = ''
p['orden_id'] = ''
p['shipping_id'] = ''
p['fecha_orden'] = '2019-12-01T12:00:00'  

lineas = []
lineas.append({
    'product_id' : 163766,
    'sku': '88963-1',
    'descripcion': 'Test product for API Guide',
    'cantidad': 1,
    'precio': 1000,
    'color': 'N/A',
    'referencia' : '125365-1'
})

p['lineas'] = lineas

pedidos=[p]

utils.getAnswer(utils.getUrl('pedidos?'), requests.post, pedidos)