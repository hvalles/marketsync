# Marketsync Documentación de API 
### Controlador de Categorias

[Inicio](https://github.com/hvalles/marketsync)
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)

El controlador se utiliza como catálogo general, lo que impica que báscamente su uso sera de lectura.

Las rutas adminitas en este controlador son las siguientes

#### Verbo: GET /categorias

Listado de categorias vigentes, de forma predeterminada el portal limita a 250 registros por consulta, por lo que de requerir menos
puede utilizar el párametro limit=N en conjunto con el parámetro offset, de no especificarse offset el valor será 0.

URL:
https://sandbox.marketsync.mx/api/categorias?ids=9350&timestamp=2019-12-12T10%3A50%3A54.289000&token=e889f7ab1ce3f97c7cc64b7fa43e84af&version=1.0&signature=ad9237253811c54c7c96a171dbce23d12f32a3c062fb778e4feff95041bcc261

Respuesta:
```JSON
{
    "answer": {
        "result": {
            "id": "9350",
            "categoria": "PIES PRENSATELAS",
            "ruta": "ELECTRODOMESTICOS/ARTEFACTOS_PARA_EL_HOGAR/MÃQUINAS_DE_COSER_Y_ACCESORIOS/ACCESORIOS/PIES_PRENSATELAS",
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

#### Verbo: GET /categorias/Atributos

Listado de categorias vigentes, de forma predeterminada el portal limita a 250 registros por consulta, por lo que de requerir menos
puede utilizar el párametro limit=N en conjunto con el parámetro offset, de no especificarse offset el valor será 0.





