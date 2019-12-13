# Marketsync Documentación de API 
### Controlador de Productos

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza para dar mantenimiento al catálogo de productos, contiene todas las acciones http.

En el caso del verbo **delete**, se espera que el producto no haya sido publicado en algún  MarketPlace, de lo contrario tendra simplemente que agotar (vea acción mas adelante) el producto.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /productos

Listado de productos actuales, puede realizar filtros a través de los parametros de ids, skus, model, name y/o brand.

URL:
```HTTP
https://sandbox.marketsync.mx/api/productos?limit=1&timestamp=2019-12-12T15%3A47%3A37.234000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=27f8be294fc5599bc0aea10295d7d541a6a708251ccfebd1e4b74279eaff90a1
```

[:link: Puede ver la composición del URL en el siguiente enlace.](https://github.com/hvalles/marketsync/blob/master/links/url.md)

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
                {
                    "id": "1",
                    "market": "Claro",
                    "precio": "599.0000",
                    "oferta": "599.0000",
                    "estado": "publicar"
                },
                {
                    "id": "2",
                    "market": "Linio",
                    "precio": "599.0000",
                    "oferta": "599.0000",
                    "estado": "publicar"
                },
                {
                    "id": "4",
                    "market": "Mercado",
                    "precio": "599.0000",
                    "oferta": "599.0000",
                    "estado": "publicar"
                },
                {
                    "id": "5",
                    "market": "Walmart",
                    "precio": "599.0000",
                    "oferta": "599.0000",
                    "estado": "publicar"
                }
            ],
            "markets": [
                {
                    "market_id": null,
                    "market": "Amazon",
                    "market_sku": null,
                    "referencia": null,
                    "activo": null,
                    "fecha": null
                },
                {
                    "market_id": null,
                    "market": "Claro",
                    "market_sku": null,
                    "referencia": null,
                    "activo": null,
                    "fecha": null
                },
                {
                    "market_id": null,
                    "market": "Linio",
                    "market_sku": null,
                    "referencia": null,
                    "activo": null,
                    "fecha": null
                },
                {
                    "market_id": "4",
                    "market": "Mercado",
                    "market_sku": "MLM550015590",
                    "referencia": "https://articulo.mercadolibre.com.mx/MLM-550015590-2-radios-comunicacion-portatil-retevis-2-vias-h-777-no-vhf-_JM",
                    "activo": "0",
                    "fecha": "2019-09-28 11:56:13"
                },
                {
                    "market_id": null,
                    "market": "Walmart",
                    "market_sku": null,
                    "referencia": null,
                    "activo": null,
                    "fecha": null
                }
            ],
            "atributos": [
                {
                    "id": "558964",
                    "atributo": "BRAND",
                    "nombre": "Marca",
                    "product_id": "162582",
                    "atributo_id": "BRAND",
                    "valor": "New Wave",
                    "up2date": "0"
                },
                {
                    "id": "558965",
                    "atributo": "LINE",
                    "nombre": "LÃ­nea",
                    "product_id": "162582",
                    "atributo_id": "LINE",
                    "valor": "Radios 2 Vias",
                    "up2date": "0"
                },
                {
                    "id": "558966",
                    "atributo": "MODEL",
                    "nombre": "Modelo",
                    "product_id": "162582",
                    "atributo_id": "MODEL",
                    "valor": "T-8000",
                    "up2date": "0"
                },
                {
                    "id": "558967",
                    "atributo": "FREQUENCY_TYPE",
                    "nombre": "Tipo de frecuencia",
                    "product_id": "162582",
                    "atributo_id": "FREQUENCY_TYPE",
                    "valor": "400-470mhz",
                    "up2date": "0"
                },
                {
                    "id": "558969",
                    "atributo": "NUMBER_OF_RADIOS",
                    "nombre": "Cantidad de radios",
                    "product_id": "162582",
                    "atributo_id": "NUMBER_OF_RADIOS",
                    "valor": "1",
                    "up2date": "0"
                },
                {
                    "id": "558971",
                    "atributo": "RANGE",
                    "nombre": "Alcance",
                    "product_id": "162582",
                    "atributo_id": "RANGE",
                    "valor": "5 km",
                    "up2date": "0"
                },
                {
                    "id": "558972",
                    "atributo": "MIN_FREQUENCY",
                    "nombre": "Frecuencia mi­nima",
                    "product_id": "162582",
                    "atributo_id": "MIN_FREQUENCY",
                    "valor": "400 MHz",
                    "up2date": "0"
                },
                {
                    "id": "558973",
                    "atributo": "MAX_FREQUENCY",
                    "nombre": "Frecuencia maxima",
                    "product_id": "162582",
                    "atributo_id": "MAX_FREQUENCY",
                    "valor": "470 MHz",
                    "up2date": "0"
                },
                {
                    "id": "558974",
                    "atributo": "GTIN",
                    "nombre": "Codigo universal de producto",
                    "product_id": "162582",
                    "atributo_id": "GTIN",
                    "valor": "N/A",
                    "up2date": "0"
                },
                {
                    "id": "558978",
                    "atributo": "POWER",
                    "nombre": "Potencia",
                    "product_id": "162582",
                    "atributo_id": "POWER",
                    "valor": "5 W",
                    "up2date": "0"
                },
                {
                    "id": "558979",
                    "atributo": "VOX_FUNCTION",
                    "nombre": "Con funciÃ³n vox",
                    "product_id": "162582",
                    "atributo_id": "VOX_FUNCTION",
                    "valor": "SÃ­",
                    "up2date": "0"
                },
                {
                    "id": "558982",
                    "atributo": "BATTERY_CAPACITY",
                    "nombre": "Capacidad de la baterÃ­a",
                    "product_id": "162582",
                    "atributo_id": "BATTERY_CAPACITY",
                    "valor": "1500 mAh",
                    "up2date": "0"
                },
                {
                    "id": "558983",
                    "atributo": "BATTERY_LIFE",
                    "nombre": "DuraciÃ³n de la baterÃ­a",
                    "product_id": "162582",
                    "atributo_id": "BATTERY_LIFE",
                    "valor": "8 h",
                    "up2date": "0"
                },
                {
                    "id": "558984",
                    "atributo": "ITEM_CONDITION",
                    "nombre": "Condicion del I­tem",
                    "product_id": "162582",
                    "atributo_id": "ITEM_CONDITION",
                    "valor": "Nuevo",
                    "up2date": "0"
                },
                {
                    "id": "558988",
                    "atributo": "SELLER_SKU",
                    "nombre": "SKU",
                    "product_id": "162582",
                    "atributo_id": "SELLER_SKU",
                    "valor": "8811X",
                    "up2date": "0"
                },
                {
                    "id": "558992",
                    "atributo": "PACKAGE_LENGTH",
                    "nombre": "Largo del paquete",
                    "product_id": "162582",
                    "atributo_id": "PACKAGE_LENGTH",
                    "valor": "19.5 cm",
                    "up2date": "0"
                },
                {
                    "id": "558993",
                    "atributo": "PACKAGE_WEIGHT",
                    "nombre": "Peso del paquete",
                    "product_id": "162582",
                    "atributo_id": "PACKAGE_WEIGHT",
                    "valor": "75 g",
                    "up2date": "0"
                },
                {
                    "id": "558994",
                    "atributo": "PACKAGE_WIDTH",
                    "nombre": "Ancho del paquete",
                    "product_id": "162582",
                    "atributo_id": "PACKAGE_WIDTH",
                    "valor": "18 cm",
                    "up2date": "0"
                },
                {
                    "id": "558995",
                    "atributo": "PACKAGE_HEIGHT",
                    "nombre": "Altura del paquete",
                    "product_id": "162582",
                    "atributo_id": "PACKAGE_HEIGHT",
                    "valor": "10.5 cm",
                    "up2date": "0"
                }
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
                    "product_id": "162582",
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
                        {
                            "id": "1447206",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "2",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447207",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "3",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447208",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "4",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447209",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "5",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447210",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "6",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447211",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "7",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447212",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "8",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447213",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "9",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        },
                        {
                            "id": "1447214",
                            "cliente_id": "1005",
                            "sku_cte": "8811X",
                            "product_id": "162582",
                            "orden": "10",
                            "recurso_id": "1",
                            "url": "http://mlm-s1-p.mlstatic.com/",
                            "fecha": "2019-10-14 00:57:11"
                        }
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
****- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss



#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)

