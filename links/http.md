# Marketsync Documentación de API 
### Seccion de comandos http

[Inicio](https://github.com/hvalles/marketsync)

### Los comandos http utilizados en el consumo del API se describen a continuación

|Comando | Uso | Significado |
|------- | --- | ----------- 
|GET |Obtener Listados|Consultas a la base de datos del cliente correspondiente o de catálogos generales|
|POST|Insertar registros|Agregar información a la base de datos, correspondiente al cliente|
|PUT|Actualizar registros|Actualizar información existente, a la base de datos correspondiente al cliente|
|DELETE|Eliminar Registros|Remover registros de la base de datos perteneciente al cliente|

### Las APIs se encuentran divididas en secciones 
De acuerdo al controlador de cada modelo y se limitan solamente a la funcionalidad expuesta por el diseño, es decir no todos los comandos aplican por cada controlador, usualmente los catálogos generales solamente podrás consultarlos.

[Ver Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)

#### Lista de comandos aplicables a los controladores

|Controlador|Descripción|GET|POST|PUT|DELETE|
|-----------|-----------|---|----|---|------|
|Categorias|Catálogo general de las categorías habilitadas|:white_check_mark:|:x:|:x:|:x:|
|Colores|Catálogo general de colores válidos|:white_check_mark:|:x:|:x:|:x:|
|Markets|Catálogo general de Marketplaces activos|:white_check_mark:|:white_check_mark:|:x:|:x:|
|Paises|Catálogo general de países admitidos|:white_check_mark:|:x:|:x:|:x:|
|Pedidos|Entrada de Pedidos por MarketPlace |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:|
|Precios|Precios por producto por MarketPlace |:white_check_mark:|:x:|:white_check_mark:|:x:|
|Productos|Mantenimiento al maestro de productos |:white_check_mark:|:white_check_mark:|:white_check_mark:|:white_check_mark:|
|Stock|Mantenimiento al stock de cada variación |:white_check_mark:|:white_check_mark:|:white_check_mark:|:x:|
|Usuarios|Catálogo general de usuarios del cliente|:white_check_mark:|:x:|:x:|:x:|

> :information_source: Importante
> Cualquier petición a un controlador con un verbo no admitido respondera con un error 404:
> 'Method is not allowed or does not exists.'
