# Marketsync Documentación de API 
### Controlador de Stock

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para actualizar la Ubicación y el Stock de las variaciones
> :information_source: Importante
> La ubicación que se obtiene al entrar un pedido se refiere a la última entrada de la misma con stock mayor que cero y
solamente se recupera a través del API de pedidos

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /ubicado

Listado de existencias de variaciones, mismos que puede ser filtrado por ids,skus de productos.

URL:
```HTTP
http://sandbox.marketsync.mx/api/ubicado?timestamp=2021-08-17T17%3A57%3A09.093250&token=a00c96f3a33de16f50ac1ab47222f232&version=1.0&signature=74c8d3ea37e7efc3273b5ce797b7df2921673c7ad61722cee5da12813821be22

```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer":
    [
        {
            "sku": "0697-1000-0010",
            "ubicacion": "INC-001",
            "actual": "2021-08-17 18:14:11",
            "id": "1",
            "stock": "1"
        },
        {
            "sku": "0697-1000-0010",
            "ubicacion": "INC-002",
            "actual": "2021-08-17 18:14:11",
            "id": "3",
            "stock": "4"
        },
        {
            "sku": "0697-1000-0020",
            "ubicacion": "INC-001",
            "actual": "2021-08-17 18:14:11",
            "id": "2",
            "stock": "2"
        },
        {
            "sku": "0697-1000-0020",
            "ubicacion": "INC-002",
            "actual": "2021-08-17 18:14:11",
            "id": "4",
            "stock": "5"
        },
        {
            "sku": "0697-1000-0025",
            "ubicacion": "INC-003",
            "actual": "2021-08-17 18:14:11",
            "id": "5",
            "stock": "6"
        }
    ],
    "timestamp": "2021-08-17 18:14:11"
}

```

- **id** es el identificador del registro.
- **sku** es el sku de la variación.
- **stock** cantidad de stock actual de la variación
- **ubicacion** Ubicacion del existencia del producto
- **actual** Timestamp de actualización
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: POST /stock

Llamado para inserción y/o actualización del stock de productos y sus ubicaciones.

URL:
```HTTP
http://sandbox.marketsync.mx/api/ubicado?timestamp=2019-12-12T10%3A52%3A37.158000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=561d0f88ad80870e55d34d40413e849a11de3afe752f493669e5ad00d9a41265
```

```python
import requests
import utils # Review config.example file and rename it to config.py, do not forget to erase your keys.

# Verbo POST 
items = []
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0010', 'stock':1})
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0020', 'stock':2}) 
items.append({'ubicacion':'INC-002', 'seller_sku':'0697-1000-0010', 'stock':4})
items.append({'ubicacion':'INC-002', 'seller_sku':'0697-1000-0020', 'stock':5})
items.append({'ubicacion':'INC-003', 'seller_sku':'0697-1000-0025', 'stock':6})


utils.getAnswer(utils.getUrl('ubicado?'), requests.post, items)
```
La respuesta es la misma que el get filtrando los elementos actualizados


```python
# Verbo DELETE  
items = []
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0010'})
items.append({'ubicacion':'INC-001', 'seller_sku':'0697-1000-0020'}) 
utils.getAnswer(utils.getUrl('ubicado?'), requests.delete, items)
```

Respuesta:
```javascript
{
    "answer":
    [
        {
            "sku": "0697-1000-0010",
            "ubicacion": "INC-001"
        },
        {
            "sku": "0697-1000-0020",
            "ubicacion": "INC-001"
        }
    ],
    "timestamp": "2021-08-17 18:14:11"
}
```


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)
