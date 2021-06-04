# Marketsync Documentación de API 
### Controlador de Fulfillment

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para visualizar El Stock de los productos estableciudos como Fulfillment, es decir que el

marketplace tiene la totalidad del Stock del producto en sus instalaciones.

#### Verbo: GET /fulfillment

Listado de Stock y Productos, establecidos como fulfillment. 

URL:
```HTTP
http://sandbox.marketsync.mx/api/fulfillment?timestamp=2019-12-12T10%3A52%3A33.195000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=e48273e6a215eb5afda5ea52919e698fadf90691df5a1090f90f578e279dae32
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
   "answer": [
        {
            "id": "152767",
            "parentsku": "88-382",
            "nombre": "Prenda algodón Coccolato rosa niña",
            "sku": "88-382",
            "almacen": "fulfillment",
            "stock": "3",
            "market_id": "6",
            "market": "Amazon"
        },
        {
            "id": "152769",
            "parentsku": "88-384",
            "nombre": "Prenda algodón Coccolato 2 piezas niña",
            "sku": "88-384",
            "almacen": "fulfillment",
            "stock": "0",
            "market_id": "6",
            "market": "Amazon"
        },
    ],
    "timestamp": "2020-06-22 17:56:06"
}
```

- **id** es el identificador del producto.
- **parentsku** es el sku padre del producto
- **sku** es el sku de la variación
- **nombre** nombre del producto
- **almacen** siempre fulfillment
- **stock** stock de la variación producto en el marketplace
- **market_id** es el identificador del market place.
- **market** es el nombre del marketplace

- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

