# Marketsync Documentación de API 
### Controlador de Variación

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para agregar o actualizar las variaciones de producto.

> :information_source: Importante
> La lista de atributos corresponde solamente a aquelos que sean identificados como **"variación"**

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET 

Esta acción no esta admitida, dado que las variaciones pueden ser obtenidas al momento de recuperar el pro ducto.
refierase al verbo [GET de productos](productos.md)

#### Verbo: POST
Se utiliza en la creación de nuevas variaciones, debe devolver las variaciones de los productos, a los que se le agregó un miembro.

[Ver ejemplo en python](../examples/python/variacion.py)

#### Tabla Definición de Columnas

|columna|tipo|mandatorio|descripcion|
|-------|----|----------|-----------|
|**product_id**|integer|:heavy_check_mark:|Identificador de producto|
|**sku**|string(18)|:heavy_check_mark:|Identificador de variación Seller_Sku|
|**stock**|integer|:heavy_check_mark:|Cantidad de stock|
|**color**|string(50)|:heavy_check_mark:|Color comercial de la variación|
|**base**|string(30)|:heavy_check_mark:|Identificador de color, revise el controlador de colores para ver colores válidos|
|**talla**|string(15)|:x:|Talla de la variación|
|**gtin**|string(15)|:x:|Código de barras de la variación|
|**video**|string(250)|:heavy_check_mark:|URL del video, puede enviar vacio ('') de no tener la información|
|**imagen1**|string(250)|:heavy_check_mark:|URL de imagen principal, puede enviar vacio ('') de no tener la información|
|**imagen2**|string(250)|:heavy_check_mark:|URL de imagen adicional, puede enviar vacio ('') de no tener la información|
|**imagen3**|string(250)|:heavy_check_mark:|URL de imagen adicional, puede enviar vacio ('') de no tener la información|
|**imagen4**|string(250)|:heavy_check_mark:|URL de imagen adicional, puede enviar vacio ('') de no tener la información|
|**imagen5**|string(250)|:heavy_check_mark:|URL de imagen adicional, puede enviar vacio ('') de no tener la información|
|**imagen6**|string(250)|:heavy_check_mark:|URL de imagen adicional, puede enviar vacio ('') de no tener la información|
|**imagen7**|string(250)|:x:|URL de imagen adicional, puede omitir o enviar vacio ('') de no tener la información|
|**imagen8**|string(250)|:x:|URL de imagen adicional, puede omitir o enviar vacio ('') de no tener la información|
|**imagen9**|string(250)|:x:|URL de imagen adicional, puede omitir o enviar vacio ('') de no tener la información|
|**imagen10**|string(250)|:x:|URL de imagen adicional, puede omitir o enviar vacio ('') de no tener la información|
|**bullet1**|string(250)|:heavy_check_mark:|Cadena de información adicional que se despliega como bullet, acepta vacío ''|
|**bullet2**|string(250)|:heavy_check_mark:|Cadena de información adicional que se despliega como bullet, acepta vacío ''|
|**bullet3**|string(250)|:heavy_check_mark:|Cadena de información adicional que se despliega como bullet, acepta vacío ''|
|**bullet4**|string(250)|:heavy_check_mark:|Cadena de información adicional que se despliega como bullet, acepta vacío ''|
|**bullet5**|string(250)|:heavy_check_mark:|Cadena de información adicional que se despliega como bullet, acepta vacío ''|
|**atributos**|array|:heavy_check_mark:|conjunto de atributos exclusivo de variaciones, la presencia del UPC o EAN es mandatoria en los atributos |
|**atributos.atributo**|string(50)|:heavy_check_mark:|Clave del atributo, revise el controlador de categorias en atributos|
|**atributos.valor**|string(50)|:heavy_check_mark:|Valor del atributo|


#### Verbo: PUT
Se utiliza en la creación de nuevas variaciones

#### Verbo: DELETE

Se utiliza para eliminar las variaciones, para poder hacer válido la acción, el producto no debe de haber sido publicado.

[Ver ejemplo en python](../examples/python/variacion.py)