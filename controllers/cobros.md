# Marketsync Documentación de API 
### Controlador de Cobros

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](/links/controller.md)

El controlador se utiliza como plataforma de cobro en sucursal, es válido únicamente, 
para pasarelas de "qrstore-mx"

Las rutas admitidas en este controlador son las siguientes

#### Verbo: GET /cobros

Obtiene información acerca del pedido solicitado, para procesar su pago.

URL:
```HTTP
http://sandbox.marketsync.mx/api/cobros?orders=1052&timestamp=2022-01-25T00%3A12%3A07.397602&token=a00c96f3a33de16f50ac1ab47222f232&version=1.0&signature=e3574abc5e71b3cc3dfe7b0c258a1e9112eead91be94a3b01290df22d23cecb6
```

[:link: Puede ver la composición del URL en el siguiente enlace.](/links/url.md)

Respuesta:
```javascript
{
    "answer":
    [
        {
            "id": "3",
            "store": "qrstore-mx.myshopify.com",
            "referencia": "8523697452",
            "numero": "1052",
            "total": "659.00",
            "entregara": "Benjamin Rascon",
            "cp": "66376",
            "estatus": "pending",
            "fecha": "2022-01-24 16:42:48",
            "cobrado": "0.00"
        }
    ],
    "timestamp": "2022-01-25 00:12:54"
}
```
- **id** es el identificador de la orden temporal.
- **store** es el dominio desde donde se genera
- **referencia** es el identificador interno del pedido (read only)
- **numero** es el código que recibe el cliente para procesar el pago
- **total** es el monto a cobrar
- **entregara** nombre del cliente alque se le entregará el pedido
- **estatus** debe de ser "pending"
- **fecha** es la fecha y hora de la respuesta en formato YYYY-MM-SS HH:mm:ss
- **cobrado** es lo que actualmente se ha pagado, solamente acepta un pago por orden


#### Verbo: POST /cobros

Registra el pago con el monto establecido a la orden correspondiente

URL:
```HTTP
http://sandbox.marketsync.mx/api/cobros?orders=1052&timestamp=2022-01-25T00%3A39%3A33.995217&token=a00c96f3a33de16f50ac1ab47222f232&version=1.0&signature=096ea36e4eb85f1df822242cb742009572514f05633e116cca9a6a65a339ad25
```
Body
```javascript
{
     "caja":"5",
     "monto":"659",
     "sucursal":"La Fe",
     "ticket":"123456"
}
```

Respuesta:
```javascript
{
    "answer":
    {
        "success": "Payment registered 659",
        "id": 4
    },
    "timestamp": "2022-01-25 00:39:34"
}
```

### Es importante conservar el folio del pago, si deseas cancelar posteriormente.

#### Verbo: PUT /cobros (Deprecated)

Cancela el registro del pago, la operacióin tiene un límite de tiempo para
realizarse de 60 minutos.

Se requiere el folio del pago.

URL:
```HTTP
http://sandbox.marketsync.mx/api/cobros?ids=4&timestamp=2022-01-25T00%3A44%3A32.561919&token=a00c96f3a33de16f50ac1ab47222f232&version=1.0&signature=f44a55166b34dbb068e8d93a5b0c2257941daf0403b72ee46e4308907c80003b
```

Respuesta: (Deprecated no longer active)
```javascript
{
    "answer":
    {
        "success": "Payment Canceled ",
        "id": "4"
    },
    "timestamp": "2022-01-25 00:44:32"
}
```

#### También le puede interesar:

- [Servidor](/links/server.md)
- [Ruta de Recurso](/links/url.md)
- [Conjunto de Llaves](/links/keys.md)

