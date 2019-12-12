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

[Ver Ruta de Recurso](https://github.com/hvalles/marketsync/links/url.md)

#### Lista de comandos aplicables a los controladores

|Controlador|Descripción|GET|POST|PUT|DELETE|
|-----------|-----------|---|----|---|------|
|Categorias|Catálogo general de las categorías habilitadas|:white_check_mark:|:x:|:x:|:x:|