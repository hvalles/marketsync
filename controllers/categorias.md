# Marketsync Documentación de API 
### Controlador de Categorias

[Inicio](/)  
[Controladores](/links/controller.md)

El controlador se utiliza como catálogo general, lo que impica que báscamente su uso será de lectura.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /categorias

Listado de categorias vigentes, de forma predeterminada el portal limita a 250 registros por consulta, por lo que de requerir menos
puede utilizar el párametro limit=N en conjunto con el parámetro offset, de no especificarse offset el valor será 0.

URL:
```HTTP
http://sandbox.marketsync.mx/api/categorias?ids=9350&timestamp=2019-12-12T10%3A50%3A54.289000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=ad9237253811c54c7c96a171dbce23d12f32a3c062fb778e4feff95041bcc261
```
Respuesta:
```javascript
{
    "answer": {
        "result": {
            "id": "9350",
            "categoria": "PIES PRENSATELAS",
            "ruta": "ELECTRODOMESTICOS/ARTEFACTOS_PARA_EL_HOGAR/MAQUINAS_DE_COSER_Y_ACCESORIOS/ACCESORIOS/PIES_PRENSATELAS",
            "permite_variacion": "1",
            "filtros": [
                {
                    "filtro_id": "20306",
                    "filtro": "Accesorios y Repuestos"
                },
                {
                    "filtro_id": "20294",
                    "filtro": "Batidoras y procesadores"
                },
                {
                    "filtro_id": "20286",
                    "filtro": "Cafeteras"
                },
            ]
        }
    },
    "timestamp": "2019-12-12 17:53:03"
}
```

- **id** es el identificador de la categoría.
- **categoria** es el nombre de la misma
- **ruta** se refiere al path completo desde el orgigen hasta el último nivel.
- **permite_variacion** se refiere si la categoría permite variaciones en el producto.

- **filtros**, en caso de que aplique se refieren a una subcategoría administrable para ClaroShop [Deprecated].
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss


#### Verbo: GET /categorias/Atributos

Listado de categorias vigentes, de forma predeterminada el portal limita a 250 registros por consulta, por lo que de requerir menos
puede utilizar el párametro limit=N en conjunto con el parámetro offset, de no especificarse offset el valor será 0.

```http
http://localhost:5000/api/categorias/atributos/7416?timestamp=2019-12-12T10%3A52%3A32.695000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=cdfc5539070628532c593f66942ac540d64aa6df1361f0f879e2600d7c39d307
```
Respuesta:
```javascript
{
    "answer": [
        {
            "id": "5833",
            "orden": "1",
            "atributo": "BRAND",
            "nombre": "Marca",
            "relevancia": "1",
            "tipo_valor": "string",
            "tipo_long_max": "255",
            "variacion": "0",
            "valores": [
                {
                    "id": "32408",
                    "clave": "23128",
                    "valor": "Abercrombie & Fitch"
                },
                {
                    "id": "32409",
                    "clave": "14810",
                    "valor": "Adidas"
                },
            ],
            "unidades": []
        },
        {
            "id": "5834",
            "orden": "2",
            "atributo": "LINE",
            "nombre": "Línea",
            "relevancia": "1",
            "tipo_valor": "string",
            "tipo_long_max": "255",
            "variacion": "0",
            "valores": [],
            "unidades": []
        },
        {
            "id": "5835",
            "orden": "3",
            "atributo": "MODEL",
            "nombre": "Modelo",
            "relevancia": "1",
            "tipo_valor": "string",
            "tipo_long_max": "255",
            "variacion": "0",
            "valores": [],
            "unidades": []
        },
    ],
    "timestamp": "2019-12-12 18:03:41"
}
```
Devuelve un conjunto de atributos válidos de acuerdo a cada categoría en donde:
- **id**: es el identificador del atributo
- **orden** es el consecutivo de ordenamiento para el registro
- **atributo** identificador explicito del atributo
- **nombre** denominación del atributo
- **relevancia**, importancia del mismo relevancia=1 es mandatorio
- **tipo_valor**, tipo de valor que se almacena boolean es mandatorio
- **tipo_long_max**, en caso de ser string el tipo_valor aplica conmo restricción en longitud
- **variacion**, en caso del que el atributo corresponda a una variación (no se admitira como atributo de producto [0=producto, 1=variación, 2=combinación]).
- **valores** es un listado de valores válidos
- **unidades**, en caso de ser un atributo de métricas, establece las unidaded validas que deberan acompañar al valor real, ejemplo en caso de la unidad = "cm" el valor esperado es un numero + espacio + unidad es decir "10 cm"


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

