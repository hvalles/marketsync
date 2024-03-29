# Marketsync Documentación de API 
### Controlador de Markets

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para visualizar los MarketPlaces vigentes, como para actualizar su participación en los mismos.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /markets

Listado de MarketPlaces vigentes

URL:
```HTTP
http://sandbox.marketsync.mx/api/markets?timestamp=2019-12-12T10%3A52%3A33.195000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=e48273e6a215eb5afda5ea52919e698fadf90691df5a1090f90f578e279dae32
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "1",
            "market": "Claro",
            "url_sitio": "https://www.claroshop.com/"
        },
        {
            "id": "2",
            "market": "Linio",
            "url_sitio": "https://linio.com.mx"
        },
        {
            "id": "4",
            "market": "Mercado",
            "url_sitio": "https://mercadolibre.com.mx"
        },
        {
            "id": "5",
            "market": "Walmart",
            "url_sitio": "https://www.walmart.com.mx"
        },
        {
            "id": "6",
            "market": "Amazon",
            "url_sitio": "https://www.amazon.com.mx"
        }
    ],
    "timestamp": "2019-12-12 18:38:55"
}
```

- **id** es el identificador del market.
- **market** es el nombre del mismo
- **url_sitio** es la URL del market place en particular
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: POST /markets

- Activar/Desactivar MarketPlace a petición
- Actualizar la protección del mismo

POST parametros mandatorios
- **market_id** se refiere al identificador del market Ej 6 = Amazon
- **activo** Se deseas activar = 1 o desactivar = 0 el MarketPlace.
- **proteccion** En caso de que desees activar una protección de tu stock para un Market en particulor, por Seller_Sku, aqui defines la cantidad (0-5) en unidades.

URL:
```HTTP
http://sandbox.marketsync.mx/api/markets?timestamp=2019-12-12T10%3A52%3A33.195000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=e48273e6a215eb5afda5ea52919e698fadf90691df5a1090f90f578e279dae32
```
Respuesta:
```javascript
{"answer":{"result":"Posting market Amazon is enabled, with protection 1"},"timestamp":"2019-12-12 18:45:08"}
```

- **result** es la confirmación de la acción realizada.
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

**Errores comunes**
- Error invalid/missing field market [17], el market no existe.
- Error invalid/missing field proteccion 10, must be 0-5 units.
- Error missing field Activo (1/0)"}


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

