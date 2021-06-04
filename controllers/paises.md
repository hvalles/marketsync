# Marketsync Documentación de API 
### Controlador de Paises

[Inicio](/)  
[Controladores](/links/controller.html)

El controlador se utiliza como catálogo general, lo que impica que báscamente su uso será de lectura.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /paises

Listado de países válidos, estos países se refieren al país de origen del producto, mismo qeue algunos MarketPlaces solicitan.

URL:
```HTTP
http://sandbox.marketsync.mx/api/paises?timestamp=2019-12-12T10%3A52%3A34.690000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=5e111544f6d8519780daacf7804b25a9f4d4acb892e7e272b9b4ad1461fc507c
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.html)

Respuesta:
```javascript
{
    "answer": [
        {
            "id": "4",
            "pais": "Afghanistan",
            "code": "AF",
            "code3": "AFG"
        },
        {
            "id": "8",
            "pais": "Albania",
            "code": "AL",
            "code3": "ALB"
        },
        {
            "id": "12",
            "pais": "Algeria",
            "code": "DZ",
            "code3": "DZA"
        },
        ...
    ],
    "timestamp": "2019-12-12 18:31:50"
}
```

- **id** es el identificador del país.
- **pais** es el nombre del mismo.
- **code** es el código de 2 caracteres para el país.
- **code3** se refiere al código de 3 caracteres para al país.
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss



#### También le puede interesar:

- [Servidor](/links/server.html)
- [Ruta de Recurso](/links/url.html)
- [Conjunto de Llaves](/links/keys.html)

