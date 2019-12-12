# Marketsync Documentación de API 
### Controlador de Stock

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza para actualizar el Stock de las variaciones, así como para actualizar la fecha de corte de la actualización.

> :information_source: Importante
> La fecha de actualización se utiliza para el corte de ventas, y considera a partir de esa fecha los pedidos registrados para considerarlo como venta y descontarlo del inventario.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /stock

Listado de existencias de variaciones, mismos que puede ser filtrado por ids,skus de productos.

URL:
```HTTP
https://sandbox.marketsync.mx/api/stock?ids=162700&timestamp=2019-12-12T10%3A52%3A36.686000&token=e889f7ab1ce3f97c7cc64b7fa43e84af&version=1.0&signature=54a98aea2667c308ef086195b6d2c9d0ea71efa292071e6399e91bddd0b0144c
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "146299",
            "sku": "7811P",
            "modelo": "T-78000",
            "skus": [
                {
                    "seller_sku": "78115",
                    "stock": "0",
                    "teorico": "0",
                    "color": "Negro"
                },
                {
                    "seller_sku": "78125",
                    "stock": "0",
                    "teorico": "0",
                    "color": "Negro Azabache"
                },
                {
                    "seller_sku": "8011",
                    "stock": "0",
                    "teorico": "0",
                    "color": "Khaki"
                },
            ]
        },
    ],
    "timestamp": "2019-12-12 22:26:05"
}
```

- **id** es el identificador del producto.
- **sku** es el sku del parent sku.
- **modelo** modelo del producto.
- **skus** Arreglo de variaciones
  - **seller_sku** se refiere sku de la variacion.
  - **stock** cantidad de stock actual de la variación
  - **teorico** stock teórico despues de restar protección y ventas
  - **color** color de la variación como referencia.
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss


#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

