# Marketsync Documentación de API 
##### Ultima actualización 2019-12-12 08:00
Documentación del uso de la integración de MarketSync con diferenes plataformas a través de la API.

[Portal de MarketSync](https://marketsync.mx)

Marketsync es una plataforma de integración entre multiples entidades, cuyo fn definitivo es colocar productos en el mercado a través de diferentes canalaes de venta como lo son Amazon, Merca doLibre, Claro, Linio, Walmart, etc.

De la misma forma te permite integrar múltiples plataformas con el fin de que obtengas el mayor provecho a la infraestructura 
que actualmente utilizas (Legacy) o que lo acompañes de plataformas de terceros que te apoyen a extender tus canales de venta 
en línea o locales.

Entre otras cosas podrás integrar y/o controlar.

- Catalogo de Productos
- Listas de Precios
- Stock
- Variaciones
- Marketplaces
- Imágenes
- Pedidos
  

  > Aunque existen varios mecanismos para la integración de APIS, hemos optado por utilizar [REST Representational State Transfer]
  > (https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional), ya que lo consideramos dinámico y flexible, así como 
  > sumamente difundido en el mercado actual. 

  ### Los comandos http utilizados en el consumo del API se describen a continuación

  |Comando | Uso | Significado |
  |------- | --- | ----------- 
  |GET |Obtener Listados|Consultas a la base de datos del cliente correspondiente o de catálogos generales|
  |POST|Insertar registros|Agregar información a la base de datos, correspondiente al cliente|
  |PUT|Actualizar registros|Actualizar información existente, a la base de datos correspondiente al cliente|
  |DELETE|Eliminar Registros|Remover registros de la base de datos perteneciente al cliente|

  ### Las APIs se encuentran divididas en secciones 
  De acuerdo al controlador de cada modelo y se limitan solamente a la funcionalidad expuesta por el diseño, es decir no todos los comandos aplican por cada controlador, usualmente los catálogos generales solamente podrás consultarlos.

  #### Lista de comandos aplicables a los controladores

  |Controlador|Descripción|GET|POST|PUT|DELETE|
  |-----------|-----------|---|----|---|------|
  |Categorias|Catálogo general de las categorías habilitadas|:white_check_mark:|:x:|:x:|:x:|