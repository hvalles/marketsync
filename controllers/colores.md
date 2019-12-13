# Marketsync Documentación de API 
### Controlador de Colores

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza como catálogo general, lo que impica que báscamente su uso será de lectura.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /colores

Listado de colores válidos, estos colores se refieren al color base, para el color comercial no se limita en valores; a excepción de ciertas categoría que arrojaran un conjunto de valores válidos para el caso particular.

URL:
```HTTP
https://sandbox.marketsync.mx/api/colores?timestamp=2019-12-12T10%3A52%3A34.193000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=1a7cb61e0167084310dc5a26013c0531445e5275be283aa002a13f18f1890d01
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "3",
            "color": "AMARILLO"
        },
        {
            "id": "4",
            "color": "AZUL"
        },
        {
            "id": "1",
            "color": "BEIGE"
        },
    ],
    "timestamp": "2019-12-12 18:31:50"
}
```

- **id** es el identificador del color.
- **color** es el nombre del misma
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss



#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

