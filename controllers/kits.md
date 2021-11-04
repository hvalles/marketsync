# Marketsync Documentación de API 
### Controlador de Kits

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para crear/actualizar/obtener y eliminar kits

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /kits

Listado de Kits

URL:
```HTTP
http://sandbox.marketsync.mx/api/kits?timestamp=2019-12-12T10%3A52%3A33.195000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=e48273e6a215eb5afda5ea52919e698fadf90691df5a1090f90f578e279dae32
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer":
    [
        {
            "sku": "CH-222343-206658",
            "product_id": "234890",
            "componentes":
            [
                {
                    "sku": "9871-1",
                    "nombre": "Zapatillas Abierta Emilio Bazan Tacon",
                    "id": "6233",
                    "cantidad": "1",
                    "product_id": "222343"
                }
            ],
            "fecha": "2021-10-19 10:03:27",
            "id": "5999",
            "activo": "1",
            "nombre": "Zapatillas Abierta Emilio Bazan Tacon",
            "comentario": "Prueba Update"
        }
    ],
    "timestamp": "2021-11-03 22:09:33"
}
```

- **id** es el identificador del kit.
- **sku** es el sku hijo como producto terminado.
- **comentario** comentario que aplique al kit
- **componentes** arreglo que contiene los coponentes del kit
    - **sku** sku del componente
    - **cantidad** cantidad a utilizar para el producti terminado
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: POST /kits

- Agrega un kit y desactiva los vigentes previos del mismo sku
- Restricciones
    - El componente no puede ser el producto terminaado
    - El componente no se puede repetir
    - La cantidad debe de ser mayor a 0
    - De forma predeterminada el kit se activará

URL:
```HTTP
http://sandbox.marketsync.mx/api/kits?timestamp=2019-12-12T10%3A52%3A33.195000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=e48273e6a215eb5afda5ea52919e698fadf90691df5a1090f90f578e279dae32
```
Respuesta: regresa el folio creado por sku de producto terminado
```javascript
{
    "answer":
    [
        {
            "123456": 6063
        }
    ],
    "timestamp": "2021-11-03 22:10:55"
}
```

- **result** es la confirmación de la acción realizada.
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

**Errores comunes**
- Error invalid/missing item, el producto no existe
- Error invalidqyantity, cantidad no válida.
- Error duplicated component"

#### Verbo: PUT /kits

- Modificar comentario o desactivar kit
- Restricciones
    - El kit no puede volver a ser activado

- **id** es el identificador del kit.
- **comentario** comentario que aplique al kit
- **activo** 0: desactiva

#### Verbo: DELETE /kits

- Elimina un kit de la base de datos de forma permanente
- Restricciones
    - El kit no puede estar contenido en un pedido

- **id** es el identificador del kit.


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

