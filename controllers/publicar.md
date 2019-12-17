# Marketsync Documentación de API 
### Controlador de Publicaciones

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza para emitir acciones por producto y MarketPlace, que nos brindan la oportunidad para Publicar, Suspender o Agoitar un prducto en un MarkePlace en particular.

Si por alguna razón no desea publicr un determinado producto en un MarketPlace, pero le interesa en un segmento limitado de los mismos, ya sea por alguna promoción exclusiva o por conveniencia operativa este controlador le permite realizar esa funcionalidad

Las rutas admitidas en este controlador son las siguientes

#### Verbo: PUT /productos/publicar
#### Verbo: PUT /productos/agotar
#### Verbo: PUT /productos/suspender

La diferencia entre agotar y suspender, se refiere a que en agotar probablemente tenga algún tema de inventarios y suspender sería una práctica casi definitiva para no seguir emitiendo el producto.

De manera predeterminada todos los productos se "publican" a menos de que se indique lo contrario.

La llamada es la misma, lo que varía es la accion del controlador [publicar, agotar, suspender], según sea el caso.

URL:
```HTTP
http://sandbox.marketsync.mx/api/productos/publicar?timestamp=2019-12-12T10%3A52%3A35.699000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=12b1964acc697a4b4a8c80cb3ab0db253c48dc52d1db4bee6014191fe4c28c86
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)


[Vea la implementación aqui](https://github.com/hvalles/marketsync/blob/master/examples/python/publicar.py)


Respuesta:
```javascript
    {"answer": [
        {'market_id': '1', 'id': '147670', 'market': 'Claro', 'accion': 'publicar'},
        {'market_id': '2', 'id': '147671', 'market': 'Linio', 'accion': 'publicar'},
        {'market_id': '4', 'id': '147672', 'market': 'Mercado', 'accion': 'publicar'},
        {'market_id': '5', 'id': '147673', 'market': 'Walmart', 'accion': 'publicar'},
        {'market_id': '6', 'id': '147674', 'market': 'Amazon', 'accion': 'publicar'}
    ],
    "timestamp":"2019-12-13 14:46:16"}

// En caso de que no haya cambios
    {"answer":
        { "result":"No data was modified." },
        "timestamp":"2019-12-13 14:46:16"}
```

- **msarket_id** es el identificador del MarketPlace.
- **id** es el identificador del registro
- **market** nombre del MarketPlace.
- **accion** se refiere al resultado de la acción realizada [publicar, agotar, suspender]
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss



#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

