# Marketsync Documentación de API 
### Controlador de Precios

[Inicio](/)  
[Controladores](/links/controller.html)

El controlador se utiliza como catálogo general, lo que impica que báscamente su uso será de lectura.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /precios

Listado de precios, puedes limitar la búsqueda a determinados ids o skus de productos

URL:
```HTTP
http://sandbox.marketsync.mx/api/precios?limit=5&timestamp=2019-12-12T10%3A52%3A35.181000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=7de055d3dd9c96d191fd2e44bf7c6b37956cba52bb05a7bdc8b44189845e0b25
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.html)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "142582",
            "sku": "8811",
            "modelo": "BH77",
            "nombre": "Radio de comunicación Portátil No Vhf",
            "precios": [
                {
                    "market_id": "1",
                    "market": "Claro",
                    "precio": "599.0000",
                    "oferta": "599.0000"
                },
                {
                    "market_id": "2",
                    "market": "Linio",
                    "precio": "599.0000",
                    "oferta": "599.0000"
                },
                {
                    "market_id": "4",
                    "market": "Mercado",
                    "precio": "599.0000",
                    "oferta": "599.0000"
                },
                {
                    "market_id": "5",
                    "market": "Walmart",
                    "precio": "599.0000",
                    "oferta": "599.0000"
                },
                {
                    "market_id": "6",
                    "market": "Amazon",
                    "precio": "599.0000",
                    "oferta": "599.0000"
                }
            ]
        },
    ],
    "timestamp": "2019-12-12 21:33:42"
}
```

- **id** es el identificador del país.
- **sku** es parent sku del producto
- **modelo** modelo del producto
- **nombre** nombre del producto.
- **precios** Arreglo de registros de precio por cada MarketPlace
  - **market_id** Identificador del MarketPlace
  - **market** nombre del MarketPlace
  - **precio** precio de lista del producto (debe incluir impuestos)
  - **oferta** precio al que se venderá el producto (debe incluir impuestos)
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss


#### Verbo: PUT /precios

Actualización de precios por MarketPlace, los datos de entrada corresponden a un arreglo de registros enviado en conjunto con la petición y en format JSON.

- Importante: Tener descuentos superiores al 60%, podría ocasionar que rechacen o invaliden su publicación.

```python
# Se llena el arreglo de elementos
items = []
# Los markets pueden variar consulte la lista de markets disponibles en /api/markets
items.append({'product_id':142582, 'market_id':1, 'oferta':101, 'precio':201}) # Claro
items.append({'product_id':142582, 'market_id':2, 'oferta':102, 'precio':202}) # Linio
items.append({'product_id':142582, 'market_id':4, 'oferta':104, 'precio':204}) # MeLi
items.append({'product_id':142582, 'market_id':5, 'oferta':105, 'precio':205}) # Walmart
items.append({'product_id':142582, 'market_id':6, 'oferta':106, 'precio':206}) # Amazon

# Realizando petición
r = requests.put(url, data=json.dumps(items))
```


URL:
```HTTP
http://sandbox.marketsync.mx/api/precios?limit=5&timestamp=2019-12-12T10%3A52%3A35.181000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=7de055d3dd9c96d191fd2e44bf7c6b37956cba52bb05a7bdc8b44189845e0b25
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.html)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "144700",
            "sku": "7811F",
            "modelo": "MOCHILA PARA ACAMPAR",
            "nombre": " Mochila para campismo color verde militar ",
            "precios": [
                {
                    "market_id": "1",
                    "market": "Claro",
                    "precio": "201.0000",
                    "oferta": "101.0000"
                },
                {
                    "market_id": "2",
                    "market": "Linio",
                    "precio": "202.0000",
                    "oferta": "102.0000"
                },
                {
                    "market_id": "4",
                    "market": "Mercado",
                    "precio": "204.0000",
                    "oferta": "104.0000"
                },
                {
                    "market_id": "5",
                    "market": "Walmart",
                    "precio": "205.0000",
                    "oferta": "105.0000"
                },
                {
                    "market_id": "6",
                    "market": "Amazon",
                    "precio": "206.0000",
                    "oferta": "106.0000"
                }
            ]
        }
    ],
    "timestamp": "2019-12-12 22:04:41"
}

```


#### También le puede interesar:

- [Servidor](/links/server.html)
- [Ruta de Recurso](/links/url.html)
- [Conjunto de Llaves](/links/keys.html)

