# Marketsync Documentación de API 
### Controlador de Pedidos

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza medio de procesamiento para los pedidos, obteniendo la informacion de los mismos, así coo permitiendo ingresar nuevos de tus ventas en línea.

#### Verbo: GET /pedidos

Listado de pedidos puedes filtrar la información en base a la fecha de creación, el No. de pedido, o el market al que corresponde.

URL:
```HTTP
http://sandbox.marketsync.mx/api/pedidos?after=2019-11-15T00%3A00&before=2019-11-16T00%3A00&limit=2&offset=5&timestamp=2019-12-12T10%3A52%3A31.231000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=8facfb793eacc4c224ffdea280c0cf928ffc8948b31d5893de02d124fa3fc579
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer":
    [
        {
            "id": "162958",
            "referencia": "32274456",
            "fecha_pedido": "2021-06-24 00:00:00",
            "fecha_autoriza": "2021-06-24 00:00:00",
            "total": "299.00",
            "subtotal": "257.76",
            "email": "none@claroshop.com",
            "entregara": "Roberto perez",
            "telefono": "",
            "direccion": "Lilas 1060 num int. , num ext. #7",
            "entrecalles": "Rosas y Helechos",
            "colonia": "El Invernadero",
            "ciudad": "Delegación Miguel Hidalgo",
            "estado": "Ciudad de México",
            "observaciones": "",
            "cp": "17660",
            "estatus": "embarcados",
            "guias": null,
            "orden_id": "73507",
            "shipping_id": null,
            "fecha_orden": "2021-06-24 11:46:26",
            "fecha": "2021-06-24 16:45:00",
            "envio": "0.00",
            "comision": "41.86",
            "market_id": "1",
            "market": "Claro",
            "items":
            [
                {
                    "id": "171870",
                    "pedido": "162958",
                    "product_id": "183150",
                    "sku": "61922-XG",
                    "modelo": "9603",
                    "descripcion": "Calcetas Pumas UNAM Kit 6 Pares Mixto",
                    "cantidad": "1",
                    "precio": "257.7586",
                    "color": "",
                    "variacion": "",
                    "fulfillment": "0",
                    "fecha": "2021-06-30 21:59:13",
                    "kit_id": "1244",
                    "kit":
                    [
                        {
                            "id": "1203",
                            "product_id": "180539",
                            "sku": "60834-XG",
                            "nombre": "Calcetas Pumas Unisex Blanco",
                            "color": "Blanco",
                            "talla": "XG",
                            "cantidad": "2"
                        },
                        {
                            "id": "1204",
                            "product_id": "180532",
                            "sku": "60827-XG",
                            "nombre": "Calcetas Pumas Unam Blanco",
                            "color": "Blanco",
                            "talla": "XG",
                            "cantidad": "2"
                        },
                        {
                            "id": "1205",
                            "product_id": "180534",
                            "sku": "60829-XG",
                            "nombre": "Calcetas Pumas Unam Azul",
                            "color": "Azul",
                            "talla": "XG",
                            "cantidad": "2"
                        }
                    ]
                }
            ],
            "tablas":
            [
                {
                    "tabla_id": "3",
                    "titulo_tabla": "Guías Adicionales",
                    "campo": "Mensajeria",
                    "opcion": "DHL",
                    "relacion": "id_tienda",
                    "clave": "6",
                    "titulo_extra": "No guia",
                    "extra": "253636525",
                    "comentario": "Next Day"
                }
            ]
            "ubicacion": 
            [
                {
                    "ubicacion": "INC-002", 
                    "id": "3"
                }
            ]

        }
    ],
    "timestamp": "2021-07-01 10:04:24"
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
- **tablas** Información adicional configurada por el usuario, y  alimentada sólo desde MarketSync; para propósitos de complementar su información. Es importante recalcar que cada cliente configura la infomración a sus necesidades y se 
encarga de validarla y procesala.


#### Items línea de pedido
- **id** es el identificador del renglón del pedido.
- **pedido** es el identificador del pedido.
- **product_id** identificador del producto.
- **sku** Seller Sku de la variación.
- **modelo** Modelo del producto
- **descripcion** Descripción del producto vendido
- **fulfillment** En caso de que la línea sea embarcada por el MarketPlace "1", si lo embarca el Seller "0"
- **cantidad** Cantidad vendida
- **precio** Precio unitario del producto
- **color** Color de la variación
- **variacion** Tipo de variación 
- **kit_id** Identificador de kit, en caso de existir
- **kit** Composición del kit, con las cantidades expandidas de acuerdo al Bill of Materials
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
|**linea.fulfillment**|integer|:heavy_check_mark:|Emvarcado por el MarketPlace = 1, por el Seller = 0|
|**linea.cantidad**|integer|:heavy_check_mark:|Cantidad vendida|
|**linea.precio**|decimal(15,4)|:heavy_check_mark:|Precio unitario del producto|
|**linea.color**|string(20)|:heavy_check_mark:|Color de la variación|
|**linea.referencia**|string(30)|:heavy_check_mark:|Referencia del registro en el portal|
|**linea.variacion**|string(10)|:heavy_check_mark:|Atributo que funciona como variación|

> :information_source: Importante
> Todas las fechas tienen formato YYYY-MM-DDTHH:mm:ss

#### Verbo: PUT /pedidos

Se utiliza para actualizar el estatus del pedido y agregar comentarios acerca del estado del mismo.

#### Columnas por enviar
- **referencia** Número de pedido en el market.
- **estatus** Correspondencia de estatus actual en el market.
- **comentario** Comentario por agregar en el historial.

[Ver ejemplo en python](../examples/python/pedidos.py)

Listado de  estatus por MarketPlace

|id	|market_id|market|estatus|
|---|---------|------|-------|
| 1	|1|	Claro|	Pendiente|
| 2	|1|	Claro|	entregados|
| 8	|1|	Claro|	embarcados|
| 5	|2|	Linio|	pending|
| 17|	2|	Linio|	delivered|
| 18|	2|	Linio|	canceled|
| 19|	2|	Linio|	shipped|
| 21|	2|	Linio|	failed|
| 27|	2|	Linio|	return_waiting_for_approval|
| 28|	2|	Linio|	ready_to_ship|
| 4	|4|	Mercado|	paid|
| 9	|4|	Mercado	|delivered|
| 10|	4|	Mercado|cancelled|
| 3|	5|	Walmart|WAITING ACCEPTANCE|
| 11|	5|	Walmart|CANCELED|
| 12|	5|	Walmart|RECEIVED|
| 14|	5|	Walmart|REFUSED|
| 6|	6|	Amazon|	Shipped|
| 7|	6|	Amazon|	Unshipped|
| 22|	6|	Amazon|	Canceled|
| 20|	8|	E-Commerce|	voided|
| 23|	8|	E-Commerce|	refunded|
| 24|	8|	E-Commerce|	paid|
| 25|	8|	E-Commerce|	authorized|
| 26|	8|	E-Commerce|	pending|
| 29|	8|	E-Commerce|	pendiente|


#### Verbo: GET /pedidos/totales/{id}

Recupera los cargos adicionales que tengan los pedidos, y se han identificado desde el api de consumo,
para amazon la consulta es en tiempo real, por lo que lanza una petición a su información en los
servidores del marketplace (Existe una cuota de 1 llamada cada 2 segundos)

#### Columnas por enviar
- **id** Número de pedido en MarketSync, como parte del URL

> :information_source: Importante
> Tiene que hacer una pausa de 2 segundos entre llamadas para evitar throttling


Ejemplo de respuesta
```javascript
{
    "answer":
    [
        {
            "id": 1613120,
            "pedido_id": 544888,
            "concepto": "SUBTOTAL",
            "label": "",
            "total": 904.31,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 1613121,
            "pedido_id": 544888,
            "concepto": "IVA",
            "label": "",
            "total": 144.69,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 1613122,
            "pedido_id": 544888,
            "concepto": "TOTAL",
            "label": "",
            "total": 1049,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 1613124,
            "pedido_id": 544888,
            "concepto": "PAGO_TIPO",
            "label": "Other",
            "total": 0,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 1613125,
            "pedido_id": 544888,
            "concepto": "PAGO_METODO",
            "label": "CreditCard",
            "total": 0,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 1613123,
            "pedido_id": 544888,
            "concepto": "ENVIO_COSTO",
            "label": "Shipping Draft",
            "total": 0,
            "estado": 1,
            "fecha": "2022-05-09T22:07:47"
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_INGRESOS",
            "label": "Charge Principal MXN",
            "total": 904.31,
            "estado": 1,
            "fecha": null
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_INGRESOS",
            "label": "Charge Tax MXN",
            "total": 144.69,
            "estado": 1,
            "fecha": null
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_EGRESOS",
            "label": "Fee Commission MXN",
            "total": -157.35,
            "estado": 1,
            "fecha": null
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_EGRESOS",
            "label": "Adjustment PostageBilling_FuelSurcharge MXN",
            "total": -3.16,
            "estado": 1,
            "fecha": null
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_EGRESOS",
            "label": "Adjustment PostageBilling_Postage MXN",
            "total": -74.87,
            "estado": 1,
            "fecha": null
        },
        {
            "id": 0,
            "pedido_id": 0,
            "concepto": "OTROS_EGRESOS",
            "label": "Adjustment PostageBilling_VAT MXN",
            "total": -12.48,
            "estado": 1,
            "fecha": null
        }
    ],
    "timestamp": "2022-05-12 21:03:53"
}
```

#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)
