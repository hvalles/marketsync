# Marketsync Documentación de API 
##### Ultima actualización 2019-12-12 08:00
Documentación del uso de la integración de MarketSync con diferenes plataformas a través de la API.

[Portal de MarketSync](https://marketsync.mx)

Marketsync es una plataforma de integración entre multiples entidades, cuyo fin definitivo es colocar productos en el mercado a través de diferentes canales de venta como lo son Amazon, MercadoLibre, Claro, Linio, Walmart, Elektra, Wish, Sears, etc.

De la misma forma te permite integrar múltiples plataformas con el fin de que obtengas el mayor provecho a la infraestructura que actualmente utilizas (Legacy) o que lo acompañes de plataformas de terceros que te apoyen a extender tus canales de venta en línea o locales.

Entre otras cosas podrás integrar y/o controlar.

- Catalogo de Productos
- Listas de Precios
- Kits o Combos
- Stock
- Variaciones
- Marketplaces
- Imágenes
- Pedidos
  

### Importante
- Aunque existen varios mecanismos para la integración de APIS, hemos optado por utilizar [REST Representational State Transfer]
- (https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional), ya que lo consideramos dinámico y flexible, así como sumamente difundido en el mercado actual. 

### Consideraciones especiales (24/09/2020).
- Con el objeto de facilitar la integración, la cantidad de elementos mandatorios se ha reducido significativamente
- Los elementos mandatorios serán mínimos, sin embargo se mantiene la lista de elementos que deben de estar presentes en la llamada, aunque se les asigne un valor 0 o un vacío "".
- Esto impedira que los productos se publiquen en los Marketplaces dado la carencia de algunos elementos, en caso
de que le falte información desde su integración, favor de alimentar la información de forma manual a través de las plantillas.
- Para el caso de ERPs,CRMs y otros products especializados es necesario que integres un conector (plugin), como mecanismo de comunicación entre las plataformas y los datos de nuestros clientes, puedes ver mayor información en el siguiente [enlace](https://github.com/hvalles/plugin-mks)

### Playground
- [Mostrar llamadas y sus resultados](https://sandbox.marketsync.mx/playground/index)

### Ver a continuación
- [Servidor de Pruebas](/links/server.md)
- [Obtención de juego de llaves](/links/keys.md)
- [Ruta de Recursos](/links/url.md)
- [Comandos HTTP](/links/http.md)
- [Controladores](/links/controller.md)
- [Mejores Prácticas](/links/best.md)
- [Integradores Especializados ERPs / CRMs](https://github.com/hvalles/plugin-mks)