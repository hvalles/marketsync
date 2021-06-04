# Marketsync Documentación de API 
### Seccion de URL 

[Inicio](/)

### Formacion del URL para el consumo de recursos

Para el fin de esta documentación los vínculos se direccionaran al servidor de pruebas; mismo que se limpia todos los días, una vez que hayas concluido su implementación podrá solicitar la ruta correspondiente al servidor de producción.

Las llamadas se direccionaran de acuerdo al controlador con el siguiente formato:

https://{servidor}/api/{controlador}/[{seccion}]?{token=ahyjnd}&{parametros}&{signature=ahj45d..}

- https:// Es el protocolo SSL de la llamda temporalmente sólo admitirá http
- {servidor} Para efectos de esta documentación aplicará http://sandbox.marketsync.mx
- {controlador} El controlador sobre el que desea se aplique el verbo correspondiente http.
- [ {seccion} ] opcional en caso de que el controlador admita una sección adicional
- {parámetros} Es el listado de parametros en formato GET [ ?param1=1&param2=2 ], que acompañan la petición
- {token} Se refiere a la llave pública que identifica al consumidor y al cliente con el que se le relaciona.
- {signature} Es la encriptación que identifica que la petición es reconocida y válida

Para los comandos GET esta sería toda la información necesaria, pero para POST y PUT, se requiweren información adicional,
misma que puede ser solicitada en formato formulario o en objeto JSON, dependiendo la integración.

### Listado de parametros opcionales

|Parametro|Descripcion|Ejemplo|
|---------|-----------|-------|
|ids|Se refiere a los identificadores del modelo a consultar, pueden ser varios separados por coma| &ids=1,2,3,4 |
|skus|En el caso de productos se refiere al parent sku y se utiliza para filtrar las consultas | &skus=1078,1079|
|model|Se utiliza para filtrar productos por el modelo, se admite solamente 1 modelo por petición| &model=100-365|
|brand|Filtro de productos por marca, se admite solamente 1 marca por petición| &marcas=Redberry|
|name|Filtro el contenido del modelo por nombre en un formato LIKE '%name%'| &name=Zapatilla|
|markets|Filtro el contenido del modelo de pedidos por Marketplace de acuerdo a su identificados| &markets=1,2|
|orders|Filtro el contenido del modelo de pedidos por identificador de pedido| &orders=1080,1085|
|before|Filtro el contenido del modelo de pedidos por fecha <= :before YYYY-MM-DDTHH:mm:ss| &before=2019-12-01T00:00:00|
|after|Filtra el contenido del modelo de pedidos por fecha >= :after YYYY-MM-DDTHH:mm:ss| &after=2019-11-15T00:00:00|
|beforeid|Filtro el contenido del modelo de pedidos|guias por "id" <= :beforeid | & beforeid=0|
|afterid|Filtro el contenido del modelo de pedidos|guias por "id" >= :afterid | &afterid=99999999|
|limit|Limita la cantidad de registros devueltos en la petición| &limit=50|
|offset|Ignora la cantidad de registros inicial solicitada al devolver la petición, en un valor offset=250, se ignoraran los primeros 250 renglones.| &offset=250|

#### Ejemplo URL

http://sandbox.marketsync.mx/api/categorias?ids=9350  
&timestamp=2019-12-12T10%3A50%3A54.289000  
&token=r559f7ab1cr3f97c7cc64b7fa43r54af  
&version=1.0  
&signature=ad9237253811c54c7c96a171dbce23d12f32a3c062fb778e4feff95041bcc261

En donde :
- ids hace referencia  a la categoría que deseo explorar
- timestamp es la fecha y hora de la petición en formato YYYY-MM-DDTHH:mm:ss, hora de la Cd de México
- version es la version de la API 1.0
- signature es el hash de comprobación
