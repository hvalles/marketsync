# Marketsync Documentación de API 
### Controlador de Publicaciones

[Inicio](/)  
[Controladores](/links/controller.html)

El controlador se utiliza para emitir acciones por producto y MarketPlace, que nos brindan la oportunidad para Publicar, Suspender, Fulfillment o Agotar un producto en un MarkePlace en particular.

Si por alguna razón no desea publicar un determinado producto en un MarketPlace, pero le interesa en un segmento limitado de los mismos, ya sea por alguna promoción exclusiva o por conveniencia operativa este controlador le permite realizar esa funcionalidad

Las rutas admitidas en este controlador son las siguientes

#### Verbo: PUT /productos/publicar
#### Verbo: PUT /productos/agotar
#### Verbo: PUT /productos/suspender
#### Verbo: PUT /productos/parcial
#### Verbo: PUT /productos/fulfillment

La diferencia entre agotar y suspender, se refiere a que en agotar probablemente tenga algún tema de inventarios y el marketplace será puesto en stock cero (0) y suspender sería una práctica para no emitir cambios hacia el marketplace, el producto serà administrado totalmente por el marketplace, ni descripciones, precios o stock será republicados hasta que retire de ese 
estatus.

El estatus 'parcial' indicará que solamente desea sincronizar el stock y/o precio, dejando la publicación en su descripción, ficha, nombre tal y como se encuentra en el momento de realizar el cambio.

De manera predeterminada todos los productos se "publican" a menos de que se indique lo contrario.

El estatus fulfillment, hace referencia  a los productos cuyo stock, se sadministra desde el marketplace, al colocarlo "fulfillment", solamente cambia el estado del mismo, las negociaciones se realizan directamente por el propietario con cda marketplace.

La llamada es la misma, lo que varía es la accion del controlador [publicar, agotar, prcial suspender], según sea el caso.

URL:
```HTTP
http://sandbox.marketsync.mx/api/productos/publicar?timestamp=2019-12-12T10%3A52%3A35.699000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=12b1964acc697a4b4a8c80cb3ab0db253c48dc52d1db4bee6014191fe4c28c86
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.html)


[Vea la implementación aqui](/examples/python/publicar.py)


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
- **accion** se refiere al resultado de la acción realizada [publicar, agotar, fulfillment, parcial, suspender]
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss



#### También le puede interesar:

- [Servidor](/links/server.html)
- [Ruta de Recurso](/links/url.html)
- [Conjunto de Llaves](/links/keys.html)

