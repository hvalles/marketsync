# Marketsync Documentación de API 
##### Ultima actualización 2019-12-12 08:00
Documentación del uso de la integración de MarketSync con diferenes plataformas a través de la API.

[Portal de MarketSync](https://marketsync.mx)

Marketsync es una plataforma de integración entre multiples entidades, cuyo fn definitivo es colocar productos en el mercado a través de diferentes canalaes de venta como lo son Amazon, Merca doLibre, Claro, Linio, Walmart, etc.

De la misma forma te permite integrar múltiples plataformas con el fin de que obtengas el mayor provecho a la infraestructura 
que actualmente utilizas (Legacy) o que lo acompañes de plataformas de terceros que te apoyen a extender tus canales de venta 
en línea o locales.

Entre otras cosas podrás integrar y/o controlar.

- Catalogo de Productos
- Listas de Precios
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
de que le falte información desde su integración, favor de alimentar la información de forma manual a través de las
plantillas.

### Ver a continuación
- [Servidor de Pruebas](/links/server.html)
- [Obtención de juego de llaves](/links/keys.html)
- [Ruta de Recursos](/links/url.html)
- [Comandos HTTP](/links/http.html)
- [Controladores](/links/controller.html)
- [Mejores Prácticas](/links/best.html)