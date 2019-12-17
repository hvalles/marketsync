# Marketsync Documentación de API 
### Controlador de Pedidos

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza medio de procesamiento para los pedidos, obteniendo la informacion de los mismos, así coo permitiendo ingresar nuevos de tus ventas en línea.

#### Verbo: GET /pedidos

Listado de pedidos puedes filtrar la información en base a la fecha de creación, el No. de pedido, o el market al que corresponde.

URL:
```HTTP
http://sandbox.marketsync.mx/api/pedidos?after=2019-11-15T00%3A00&before=2019-11-16T00%3A00&limit=2&offset=5&timestamp=2019-12-12T10%3A52%3A31.231000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=8facfb793eacc4c224ffdea280c0cf928ffc8948b31d5893de02d124fa3fc579
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "135851",
            "cliente_id": "1005",
            "market_id": "4",
            "referencia": "2206600680",
            "fecha_pedido": "2019-11-10 00:15:03",
            "fecha_autoriza": "2019-11-10 00:15:03",
            "subtotal": "1000",
            "total": "1160.00",
            "email": "none@ml.com",
            "entregara": "GABRIELA RAMIREZ",
            "telefono": "",
            "direccion": "Reforma 206",
            "entrecalles": "",
            "colonia": "",
            "ciudad": "Centro",
            "estado": "Guerrero",
            "observaciones": "Referencia: Portón negro Entre: Felix y Samaniego",
            "cp": "87529",
            "envio": "0.00",
            "comision": "0.00",
            "estatus": "delivered",
            "mensajeria": null,
            "guias": null,
            "estatusguia": null,
            "orden_id": null,
            "shipping_id": "",
            "fecha_orden": "2019-11-15 06:13:48",
            "fecha": "2019-12-12 14:11:04",
            "market": "Mercado",
            "items": [
                {
                    "id": "15551",
                    "pedido": "135851",
                    "product_id": "145236",
                    "sku": "5331A",
                    "modelo": "WATCH-100",
                    "descripcion": "Reloj de pared con números romanos ",
                    "cantidad": "1",
                    "precio": "1000",
                    "color": "N/D",
                    "variacion": "UNIT",
                    "fecha": "2019-11-09 22:20:02"
                }
            ]
        },
    ],
    "timestamp": "2019-12-12 21:11:54"
}

```
#### Pedido
- **id** Identificador del pedido
- **referencia** Número de pedido en el market.
- **fecha_pedido**
- **fecha_autoriza**
- **subtotal**
- **total**
- **email** Correo con el que se levanto el pedido, usualmente los MarketPlaces no lo brindan.
- **entregara** Persona que recibira elo pedido
- **telefono**
- **direccion** Calle y Número.
- **entrecalles** 
- **colonia**
- **ciudad**
- **estado**
- **observaciones** Referencia de la dirección para facilitar ubicación a paquetería.
- **cp** Código postal
- **estatus** estatu del pedido (puede variar).
- **mensajeria** nombre de la mensajería.
- **guias** úmero de Guía
- **estatusguia** 
- **orden_id** Identificador de su orden interna para procesamiento.
- **shipping_id** Consolidador de ordenes de Mercado Libre.
- **fecha_orden** fecha de creación dela orden
- **fecha** fecha de última actualización de la orden
- **market** 


#### Items línea de pedido
- **id** es el identificador del renglón del pedido.
- **pedido** es el identificador del pedido.
- **product_id** identificador del producto.
- **sku** Seller Sku de la variación.
- **modelo** Modelo del producto
- **descripcion** Descripción del producto vendido
- **cantidad** Cantidad vendida
- **precio** Precio unitario del producto
- **color** Color de la variación
- **variacion** Tipo de variación 
- **fecha** fecha del registro de la operación
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: POST /pedidos

Se utiliza en la creación de nuevos pedidos, en MarketPlace WEB

[Ver ejemplo en python](../examples/python/pedidos.py)

#### Tabla Definición de Columnas

|columna|tipo|mandatorio|descripcion|
|-------|----|----------|-----------|
|**referencia**|string(30)|:heavy_check_mark:|Número de pedido en el market.|
|**fecha_pedido**|datetime|:heavy_check_mark:|Fecha en la que se creo el pedido en el MarketPlace |
|**fecha_autoriza**|datetime|:heavy_check_mark:|Fecha en la que el pedido se pago|
|**subtotal**|decimal(15,2)|:heavy_check_mark:|Monto antes de impuestos|
|**total**|decimal(15,2)|:heavy_check_mark:|Monto con impuetos incluidos|
|**email**|string(50)|:heavy_check_mark:|Correo con el que se levanto el pedido, usualmente los MarketPlaces no lo brindan.|
|**entregara**|string(120)|:heavy_check_mark:|Persona que recibira elo pedido|
|**telefono**|string(20)|:heavy_check_mark:|Teléfono del consumidor final|
|**direccion**|string(100)|:heavy_check_mark:|Calle y Número.|
|**entrecalles**|string(100)|:heavy_check_mark:|Entre calles de la ubicaciòn de entrega|
|**colonia**|string(100)|:heavy_check_mark:|Colonia de ubicación de entrega|
|**ciudad**|string(100)|:heavy_check_mark:|Ciudad en la que se entregarán los producos|
|**estado**|string(100)|:heavy_check_mark:|Estado correspondiente a la ciudad|
|**observaciones**|string(200)|:heavy_check_mark:|Referencia de la dirección para facilitar ubicación a paquetería.|
|**cp**|string(10)|:heavy_check_mark:|Código postal|
|**estatus**|string(30)|:heavy_check_mark:|estatu del pedido (puede variar en el tiempo).|
|**mensajeria**|string(30)|:heavy_check_mark:|nombre de la mensajería.|
|**guias**|string(100)|:heavy_check_mark:|Número de Guía|
|**orden_id**|integer|:heavy_check_mark:|Identificador de su orden interna para procesamiento.|
|**shipping_id**|string(20)|:heavy_check_mark:|Consolidador de ordenes de Mercado Libre.|
|**fecha_orden**|datetime|:heavy_check_mark:|fecha de creación dela orden|
|**fecha**|datetime|:heavy_check_mark:|fecha de última actualización de la orden|
|**lineas**|array|:heavy_check_mark:|Conjunto de renglones del pedido|
|**linea.product_id**|integer|:heavy_check_mark:|identificador del producto.|
|**linea.sku**|string(18)|:heavy_check_mark:|Seller Sku de la variación.|
|**linea.descripcion**|string(120)|:heavy_check_mark:|Descripción del producto vendido|
|**linea.cantidad**|integer|:heavy_check_mark:|Cantidad vendida|
|**linea.precio**|decimal(15,4)|:heavy_check_mark:|Precio unitario del producto|
|**linea.color**|string(20)|:heavy_check_mark:|Color de la variación|
|**linea.referencia**|string(30)|:heavy_check_mark:|Referencia del registro en el portal|
|**linea.variacion**|string(10)|:heavy_check_mark:|Atributo que funciona como variación|

> :information_source: Importante
> Todas las fechas tienen formato YYYY-MM-DDTHH:mm:ss

#### Verbo: PUT /pedidos

#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

