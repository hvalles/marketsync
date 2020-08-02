# Marketsync Documentación de API 
### Controlador de Guías

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza como llamada posterior a la descarga del pedido, para recuperar información acerca de las guías. La guías, "NO" se generan de forma automática, son alimentada a través del sitio web de la aplicación que genera el pedido o a petición manual del usuario en el portal de MarketSync, dependiendo de
la plataforma a utilizar y lo que su API permita.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /guias

Listado de guías utilizadas para entregar los productos.

URL:
```HTTP
http://sandbox.marketsync.mx/api/guias?timestamp=2019-12-12T10%3A52%3A34.690000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&orders=1080,1079&signature=5e111544f6d8519780daacf7804b25a9f4d4acb892e7e272b9b4ad1461fc507c
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)

Respuesta:
```javascript
{"answer": 
[
   {
   "estatus": "1", 
   "fecha": "2020-08-01 19:27:17", 
   "mensajeria": "estafeta", 
   "label": "https://envia.com/rastreo?label=395088376888", 
   "pedido_id": "30546", 
   "id": "1294", 
   "guia": "395088376888"
   }
], 
"timestamp": "2020-08-02 17:25:26"}
```

- **id** es el identificador del registro de guías.
- **pedido** es el identificador del pedido que se envía.
- **guia** es el número de guía del embarque.
- **label** Aqui podemos encontrar 3 representaciones dependiendo el market y el resultado de la consulta.
    - Url indicando el código y sitio de rastreo de la guía
    - Cadena plana  conteniendo error al intentar generar la guía
    - Cadena en base64 que indicaría un archivo binario (pdf,zip,jpg, etc) conteniendo la guía para imprimir o en su defecto el error enmascarado en base64. 
- **mensajeria** se refiere la empresa que entrega el paquete (no siempre esta presente).
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

