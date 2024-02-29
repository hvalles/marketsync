# Marketsync Documentación de API 
### Controlador de Devoluciones

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para obtener información acerca de las devoluciones generardas en el marketplace (actualmente sopo aplica a MercadoLibre)
filtros de estado:  
- pendientes: todas las devoluciones que no han arribado
- reconocidos: devoluciones que arribaron y reconocen que llegaron
- sin-reconocer: devoluciones indicadas como que arribaron, pero no se han reconodido  


#### Verbo: GET /devoluciones

Listado de devoluciones puedes filtrar la información en base a la fecha de creación, el No. de devolución, esttaus.

URL:
```HTTP
http://sandbox.marketsync.mx/api/devoluciones?after=2019-11-15T00%3A00&before=2019-11-16T00%3A00&limit=2&offset=5&timestamp=2019-12-12T10%3A52%3A31.231000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=8facfb793eacc4c224ffdea280c0cf928ffc8948b31d5893de02d124fa3fc579
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer":
    [
        {
            "id": "89",
            "referencia": "5247082360",
            "fecha": "2024-01-28 23:53:48",
            "order_id": "1236663",
            "status_money": "refunded",
            "destination": "seller_address",
            "ref_pedido": null,
            "desde": "2024-01-29 08:16:51",
            "fecha_pedido": null,
            "market_id": "4",
            "market": "Mercado",
            "items":
            [
                {
                    "id": "89",
                    "cantidad": "1",
                    "status": "ready_to_ship",
                    "guia": "MEL43052078600FMDOR01",
                    "fecha_eta": "2024-02-02 00:00:00",
                    "descripcion": null,
                    "product_id": null,
                    "sku": null,
                    "recibe": null,
                    "fecha_dev": "2024-01-15 16:20:00",
                    "observaciones": ""
                }
            ]
        }
    ],
    "timestamp": "2024-02-29 17:53:42"
}
```
#### Devoluciones
- **id** Identificador de devolución
- **referencia** Número de devolución en el market.
- **fecha**
- **order_id** Clave de identificador del pedido en MarketSync
- **status_money** Estatus del dinero
- **destination** Hacia donde se dirige la devolución
- **ref_pedido** Refencia original del pedido.
- **desde** Fecha en la que se ingreso el registro
- **fecha_pedido** Fecha en la que se ingreso el pedido
- **market_id** Clave interna del marketplace
- **market** Marketplace

#### Items línea de devolución

- **id** es el identificador del renglón de la devolución.
- **cantidad** cantidad devuelta.
- **status** estatus de la devolución en el marketplace
- **guia** guía de envío de la mercancía
- **fecha_eta** fecha estimada de arribo
- **descripcion** Descripción del producto vendido
- **product_id** clave interna del producto
- **sku** sku del producto recibido
- **recibe** usuario que recibe la devolución 
- **fecha_dev** fecha en que la mercancía fue recibida
- **observaciones** cualquier información relevante de la mercancía recibida
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: PUT /devoluciones

Se utiliza en aceptación de la devolución

[Ver ejemplo en python](../examples/python/devoluciones.py)

#### Tabla Definición de Columnas
# row_id, devuelto, recibe_id, fecha, observaciones
|columna|tipo|mandatorio|descripcion|
|-------|----|----------|-----------|
|**row_id**|int|:heavy_check_mark:|Número de identificador del renglon.|
|**devuelto**|int|:heavy_check_mark:|Cantidad a devolver|
|**fecha**|datetime|:heavy_check_mark:|Fecha en la que se recibe la mercancía|
|**recibe_id**|int|:heavy_check_mark:|Identificador de usuario que recibe mercancía|
|**observaciones**|string(500)|:heavy_check_mark:|Cualquier informaciójn relevante acerca de la devolución|

> :information_source: Importante
> Todas las fechas tienen formato YYYY-MM-DDTHH:mm:ss


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)
