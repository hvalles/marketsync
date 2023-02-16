# Marketsync Documentación de API 
### Controlador de Categorias

[Inicio](/)  
[Controladores](/links/controller.md)

El controlador se utiliza como catálogo para tablas personalizadas que se agregan por parte del usuario, ya sea de forma manual o automática.

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /tablas

Listado de las tablas personalizadas y su configuración, 

URL:
```HTTP
http://sandbox.marketsync.mx/api/tablas?timestamp=2019-12-12T10%3A50%3A54.289000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=ad9237253811c54c7c96a171dbce23d12f32a3c062fb778e4feff95041bcc261
```
Respuesta:
```javascript
{
    "answer":
    [
        {
            "id": "19",
            "tabla": "Mercado Libre Mujer Tenis",
            "cliente_id": "0",
            "titulo_tabla": "Mercado Libre Mujer Tenis",
            "titulo_combo": "MX_SIZE",
            "titulo_llave": "210057",
            "titulo_extra": "STANDARD",
            "controlador": "GDT",
            "orden": "0"
        },
        {
            "id": "20",
            "tabla": "Mercado Libre Hombre Tenis",
            "cliente_id": "0",
            "titulo_tabla": "Mercado Libre Hombre Tenis",
            "titulo_combo": "MX_SIZE",
            "titulo_llave": "210056",
            "titulo_extra": "STANDARD",
            "controlador": "GDT",
            "orden": "0"
        },
        {
            "id": "21",
            "tabla": "Mercado Libre Mujer Botas",
            "cliente_id": "0",
            "titulo_tabla": "Mercado Libre Mujer Botas",
            "titulo_combo": "MX_SIZE",
            "titulo_llave": "259983",
            "titulo_extra": "STANDARD",
            "controlador": "GDT",
            "orden": "0"
        },
    ],
    "timestamp": "2023-02-16 18:38:40"
}

```

- **id** es el identificador de la categoría.
- **tabla** es el nombre de la misma
- **titulo_tabla** como se presenta en la captura.
- **titulo_combo** identificador del combo en la captura
- **titulo_llave** identificdor de la llave a alimentar
- **titulo_extra** en caso de requerir información adicional
- **controlador** desde que controlador se presenta la captura
- **timestamp** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss


#### Verbo: GET /tablas/detalle/{id}

Listado del detalle de la tabla, para revision de los registros pertenecientes a la misma.

```http
http://sandbox.marketsync.mx/api/tabkas/detalle/1150?timestamp=2019-12-12T10%3A52%3A32.695000&token=r559f7ab1cr3f97c7cc64b7fa43r54af&version=1.0&signature=cdfc5539070628532c593f66942ac540d64aa6df1361f0f879e2600d7c39d307
```
Respuesta:
```javascript
{
    "answer":
    [
        {
            "id": "1677",
            "tabla_id": "1150",
            "opcion": "11.5 MX",
            "llave": "448665:1",
            "activo": "1"
        },
        {
            "id": "1678",
            "tabla_id": "1150",
            "opcion": "12 MX",
            "llave": "448665:2",
            "activo": "1"
        },
        {
            "id": "1679",
            "tabla_id": "1150",
            "opcion": "12.5 MX",
            "llave": "448665:3",
            "activo": "1"
        },
    ],
    "timestamp": "2023-02-16 18:46:24"
}

```
Devuelve un conjunto de atributos válidos de acuerdo a cada categoría en donde:
- **id**: es el identificador del atributo
- **tbla_id** es el identificador del registro padre
- **opcion** la descripción de la opción a publicar
- **llave** es el valor seleccionado mediante la opción


#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

