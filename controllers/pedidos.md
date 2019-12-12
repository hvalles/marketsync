# Marketsync Documentación de API 
### Controlador de Pedidos

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza medio de procesamiento para los pedidos, obteniendo la informacion de los mismos, así coo permitiendo ingresar nuevos de tus ventas en línea.

#### Verbo: GET /pedidos

Listado de pedidos puedes filtrar la información en base a la fecha de creación, el No. de pedido, o el market al que corresponde.

URL:
```HTTP
https://sandbox.marketsync.mx/api/pedidos?after=2019-11-15T00%3A00&before=2019-11-16T00%3A00&limit=2&offset=5&timestamp=2019-12-12T10%3A52%3A31.231000&token=e889f7ab1ce3f97c7cc64b7fa43e84af&version=1.0&signature=8facfb793eacc4c224ffdea280c0cf928ffc8948b31d5893de02d124fa3fc579
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
- **cliente_id** Número interno del cliente
- **market_id** Identificador del MarketPlace
- **referencia** Nímero de pedido en el market.
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


#### Verbo: PUT /pedidos

#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

