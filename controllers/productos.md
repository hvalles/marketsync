# Marketsync Documentación de API 
### Controlador de Productos

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza para dar mantenimiento al catálogo de productos, contiene todas las acciones http.

En el caso del verbo **delete**, se espera que el producto no haya sido publicado en algún  MarketPlace, de lo contrario tendra simplemente que agotar (vea acción mas adelante) el producto.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /productos

Listado de productos actuales, puede realizar filtros a través de los parametros de ids, skus, model, name y/o brand.

URL:
```HTTP
http://sandbox.marketsync.mx/api/productos?limit=1&timestamp=2019-12-12T15%3A47%3A37.234000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=27f8be294fc5599bc0aea10295d7d541a6a708251ccfebd1e4b74279eaff90a1
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript

{
    "answer": [
        {
            "id": "1462582",
            "cliente_id": "1005",
            "nombre": "Radio Comunicación Portátil No Vhf",
            "descripcion": "MISING DESCRIPTION",
            "ficha": "is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "alto": "0.00",
            "ancho": "0.00",
            "largo": "0.00",
            "peso": "0.000",
            "precio": "599.00",
            "oferta": "599.00",
            "stock": "0",
            "sku": "8811",
            "dias_embarque": "2",
            "categoria": "CELULARES_Y_TELEFONIA/EQUIPOS_DE_RADIOFRECUENCIA/PORTATILES",
            "filtro": "",
            "marca": "New Wave",
            "categoria_id": "2752",
            "filtro_id": "0",
            "marca_id": "23240",
            "etiquetas": "",
            "etiquetas_web": "",
            "modelo": "H777",
            "activo": "0",
            "fecha": "2019-10-31 17:38:49",
            "precios": [
                {
                    "id": "6",
                    "market": "Amazon",
                    "precio": "599.0000",
                    "oferta": "599.0000",
                    "estado": "publicar"
                },
                ...
            ],
            "markets": [
                {
                    "market_id": "4",
                    "market": "Mercado",
                    "market_sku": "MLM550015590",
                    "referencia": "https://articulo.mercadolibre.com.mx/MLM-550015590-2-radios-comunicacion-portatil-retevis-2-vias-h-777-no-vhf-_JM",
                    "activo": "0",
                    "fecha": "2019-09-28 11:56:13"
                },
                ...
            ],
            "atributos": [
                {
                    "id": "558964",
                    "atributo": "BRAND",
                    "nombre": "Marca",
                    "product_id": "1462582",
                    "atributo_id": "BRAND",
                    "valor": "New Wave",
                    "up2date": "0"
                },
                ...
            ],
            "origen": "0",
            "warranty": "Garanti­a del vendedor: 30 di­as",
            "listing_type_id": "gold_special",
            "p_condition": "new",
            "nombre_modelo": "",
            "palto": null,
            "pancho": null,
            "plargo": null,
            "ppeso": null,
            "color": "",
            "base": "",
            "variaciones": [
                {
                    "id": "5020",
                    "cliente_id": "1005",
                    "sku": "8811X",
                    "product_id": "1462582",
                    "stock": "0",
                    "base": "",
                    "color": "",
                    "teorico": "0",
                    "imagen": [
                        {
                            "id": "1447205",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "1642582",
                            "orden": "1",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        ...
                    ],
                    "bullet": [],
                    "video": null,
                    "atributos": []
                }
            ]
        }
    ],
    "timestamp": "2019-12-12 22:48:21"
}


```

- **id** es el identificador del producto.
- **cliente_id** identificsador interno de la empresa.
- **nombre** nombre del producto
- **descripcion**, descripcion del producto
- **ficha** ficha técnica del producto
- **alto** alto en centímetros del producto
- **ancho** ancho del producto en centímetros
- **largo** largo del producto en centímetros
- **peso** peso del producto en kilogramos
- **sku** Parent Sku del producto.
- **dias_embarque** días de preparación para envío del producto.
- **categoria** ruta completo de categoría
- **filtro** subcategoría para uso exclusivo de ClaroShop
- **marca** nombre marca del producto
- **categoria_id** identificador interno de la categoría
- **filtro_id** identificador del filtro
- **marca_id** identificador interno de marca
- **etiquetas** etiquetas de búsqueda
- **modelo**
- **fecha**, fecha de actualización del producto
- **origen** identificador del pais de origen (consulte el controlador de Paises para más información)
- **warranty** garantía del producto, debe de ir en el formato (n) días|meses|años, donde (n) es un número entero, todos los valores son plurales.
    - Ejemplo en Días:  30 días
    - Ejemplo en Meses: 2 meses
    - Ejemplo en Años: 2 años
    - Garantía de Fabrica:
    - Garantía de fábrica: 15 días
    - Garantía de fábrica: 15 meses
    - Garantía de fábrica: 15 años

- **listing_type_id** Tipo de listado [bronze, silver, gold_pro, gold_premium, gold_special, gold]
- **p_condition** inveriablemente todos los productos serán nuevos.
- **nombre_modelo** en caso de existir un nombre comercial al modelo
- **palto** altura del paquete en centímetros
- **pancho** ancho del paquete en centímetros
- **plargo** largo del paquete en centímetros
- **ppeso** peso del paquete en kilogramos.
- **etiquetas_web** etiquetas de filtro e-commerce en portales Web (Shopify)
- **taxcode** Código de producto del SAT http://pys.sat.gob.mx/PyS/catPyS.aspx.
- **color** color comercial del producto 
- **base** color base del producto, (consulte el controlador Colores para mayor información)
- **variaciones** Conjunto de variaciones del producto
    - **id** identificador de la variación
    - **sku** seller sku, de la variación
    - **stock** existencia del producto
    - **base** color base de la variación
    - **color** color comercial de la variación
    - **teorico** inventario teórico después de descontar ventas y protección
    - **imagen** conjunto de imagenes de la variación
        - **id** identificador del recurso
        - **sku_cte** sku de la variación
        - **orden** orden de depliegue del recurso
        - **recurso_id** tipo de recurso 1=imagen
        - **url** url del recurso, MarketSync no almacena las imágenes, por lo que los recursos deben de estar vigentes, no duplicados y medir más de 200px y menos de 2000px.
        - **fecha** fecha de registro del recurso
    - **bullet** Es un conjunto de recursos (1-5) que utilizan el mismo esquema que las imagenes pero con identificadores 101-105 y recurso_id=4, ademas en lugar de una URL el valor es una cadena descriptiva como punto a resaltar del producto.
    - **video** Es un recurso (1) que utilizan el mismo esquema que las imagenes pero con identificador 99 y recurso_id=2.
    - **atributos** conjunto de atributos particulares de la variación
      - **id** identificador del registro
      - **atributo** clave del atributo
      - **nombre** nombre del atributo
      - **valor** valor del atributo
- **precios** conjunto de precios por MarketPlace
    - **id** Identificador del MarketPlace
    - **market** Nombre del ]MarketPlace
    - **precio** precio de lista (debe incluir impuestos)
    - **oferta** precio de venta (debe incluir impuestos)
    - **estado** estado del prducto en el Market [publicar, suspender, agotar]
- **markets** especificaciones de cada MarketPlace
    - **market_id** identificador del MarketPlace
    - **market**    nombre del MarketPlace
    - **market_sku** Sku con el que se registro en el MarketPlace
    -**referencia** Información adicional del registro
    - **activo** estado actual de la publicación
    - **fecha** fecha en la que se registro el producto
- **atributos** conjunto de atributos específicos de la categoría para el producto
    - **id** identificador del registro
    - **atributo** clave del atributo
    - **nombre** nombre del atributo
    - **valor** valor del atributo
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss

#### Verbo: POST /productos

Se utiliza en la creación de nuevos productos

[Ver ejemplo en python](../examples/python/productos.py)

#### Tabla Definición de Columnas

|columna|tipo|mandatorio|descripcion|
|-------|----|----------|-----------|
|nombre|string(120)|:heavy_check_mark:|Nombre del producto asegurese de que los primeros 60 caracteres describan adecuadamente al producto|
|descripcion|string(250)|:heavy_check_mark:|Resumen de la ficha técnica del producto, algunos markets la reflejan|
|ficha|string(5000)|:heavy_check_mark:|Ficha técnica detallada del producto, asegúrese de que los primeros 1500 carácteres reflejen la información necesaria, alguns markets limitan la longitud de la misma|
|alto|integer|:heavy_check_mark:|Altura del producto en centímetros|
|ancho|integer|:heavy_check_mark:|Ancho del producto en centímetros|
|largo|integer|:heavy_check_mark:|Largo  del producto en centímetros|
|peso|integer|:heavy_check_mark:|Peso del producto en kilogramos|
|sku|string(18)|:heavy_check_mark:|Parent Sku del producto procure que tenga entre 5 y 18 caracteres de longitud y es un identificador único, por lo mismo no admite actualizaciones.|
|dias_embarque|integer|:heavy_check_mark:|Días de preparación del producto|
|categoria_id|integer|:heavy_check_mark:|Identificador de la categoría Revise el controlador de categorías para amyor información|
|filtro_id|integer||Identificador del filtro como subcategoría, depende de la categoría|
|marca|string(50)|:heavy_check_mark:|Nombre de la marca|
|etiquetas|string(200)|:heavy_check_mark:|Términos de búsqueda para el producto|
|modelo|string(30)|:heavy_check_mark:|Número de modelo|
|listing_type_id|string(50)|:heavy_check_mark:|Son de Mercado Libre y afecta el % de comisión [bronze, silver, gold_pro, gold_premium, gold_special, gold](https://developers.mercadolibre.com.mx/es_ar/tipos-de-publicacion-y-actualizaciones-de-articulos) |
|warranty|string(50)||Garantía del producto|
|nombre_modelo|string(50)||Nombre comercial del modelo|
|origen|integer|:heavy_check_mark:|País de origen, vea el controlador Paises para mayor información|
|color|string(50)|:heavy_check_mark:|Color comercial del producto|
|base|string(50)|:heavy_check_mark:|Color base del producto, vea el controlador de Colores para mayor información|
|palto|integer|:heavy_check_mark:|Altura del paquete en centímetros|
|pancho|integer|:heavy_check_mark:|Ancho del paquete en centímetros|
|plargo|integer|:heavy_check_mark:|Largo del paquete en centímetros|
|ppeso|integer|:heavy_check_mark:|Peso del paquete en kilogramos|
|etiquetas_web|string(500)||Etiquetas a proporcionar a portales Web para creación de filtros entre otros. (Shopify)|
|taxcode|string(20)||Código de producto del SAT|
|date_created|DateTime|:heavy_check_mark:|Fecha en la que el producto se comercializa, aparece en algunos markets|
|atributos|Array|:heavy_check_mark:|Mandatorio en caso de llevar categoría, son los atributos de producto de acuerdo a la categoría, vea controlador Categoria/Atributos para mayor información|
|atributo.atributo_id|string(50)|:heavy_check_mark:|Identificador clave del atributo|
|atributo.valor|string(50)|:heavy_check_mark:|Valor correspondiente al atributo del producto|


> :information_source: Importante
> El listado de atributos es de acuerdo a la categoría, en caso de que el atributo sea considerado como una variación, no deberá incluirlo en este segmento, dado que existe un controlador para las variaciones en donde si aplicaría.


> :information_source: Importante
> El color y la base a este nivel se mantienen por compatibilidad, pero cada variación debe de aportar la información correspondiente.

#### Verbo: PUT /productos

Actualización del catálogo, el esquema y las columnas son las mismas con algunas restricciones, a excepción del identificador de producto product_id integer, y el sku, el resto de las columnas debe ser validada para ser modificada.
Solamente debe de incluir las columnas que sufrirán alguna alteración, las que se mantienen no tienen porque incluirlas.
Es importante mencionar que la actualización de producto emitirá una acción de republicación, para el nombre, descripción, ficha y otros elementos en los market places.

Columnas aptas para actualización.

1. nombre
2. descripcion
3. ficha
4. alto
5. largo
6. ancho
7. peso
8. dias_embarque
9. marca
10. etiquetas
11. modelo
12. warranty
13. nombre_modelo
14. origen
15. palto
16. plargo
17. pancho
18. ppeso
19. etiquetas_web
20. date_created
21. atributos

La respuesta serás similar a una consulta get con las columnas actualizadas.

[Ver ejemplo en python](../examples/python/productos.py)

#### Verbo: DELETE /productos

Se utiliza para la eliminacion de registro, la restricción es que el producto no haya sido  publicado en algún MarketPlace
o se emitirá un error al intentar ejercer la acción.

[Ver ejemplo en python](../examples/python/productos.py)

Respuesta:
```javascript
    {"answer":{"result":"Item(s) removed."},"timestamp":"2019-12-13 22:18:37"}
```

#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

