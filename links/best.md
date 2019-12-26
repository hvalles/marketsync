# Marketsync Documentación de API 
### Mejoires Prácticas

[Inicio](https://github.com/hvalles/marketsync)  
[Controladores](https://github.com/hvalles/marketsync/blob/master/links/controller.md)


A continuación se detallan algunas bases y puntos e vista que le pueden permitir utilizar esta guía de forma adecuada y productiva.

1. Lea por favor las secciones al pie de esta página.
2. Para la generación del conjunto de llaves, se requiere tener una cuenta activa, revise el portal para mayor información.
3. Recomendaciones iniciales.
   1. Revise los catálogos generales que son auxiliares para la inserción de los catalogos de productos.
      1. Colores
      2. Países
      3. Categorías
      4. Markets
   2. La categorías son fundamentales y es una parte escencial del proceso de alta de productos, revise las categorías en las que necesita empatar sus productos, antes de iniciar, esto le va a ahorrar tiempo y evitar problemas posteriores.
   3. La gama de colores es la base, los colores comerciales (Ferrero, Miel, etc.) son prácticamente libres y restringidos solamente por la longitud de caracteres (procure mantenerlo debajo de 20) y algunos Markets de forma independiente; restringen algunas palabras que se prestan a confusión, Color Tabaco, se puede malinterpretar por los validadores de descripción de los Marketplaces y asumir que se esta ofertando algún tipo de cigarrilo, Champagne puede incurrir en el mismo problema.
   4. Las dimensiones Largo, Ancho, Alto, y Peso, son escenciales, tanto para el producto, como para el paquete, procure tenerlas antes de iniciar el proceso.
   5. Algunos markets requieren de UPC/EAN, mismos que son códigos de identificación de producto, estos son relativamente económicos, estos códigos se generan por variación de proiducto, si requiere mayor información, solicite apoyo a su distribuidor, con gusto lo apoyará.
   6. Las imágenes son escenciales, y es importante contar con imágenes de calidad, el máximo de pixeles permitidos es de 2000px y el mínimo es de 200px; una imagen de calidad tiene almenos 500px, deberán de tener fondo blanco, no debería de tener articulos adicionales al producto que se oferta y que podría malinterpretar el consumidos. Así mismo las imágenes son por variación, así que si su producto tiene variaciones por color, es conveniente que invierta el tiempo necesario para considerar las imagenes de cada color.
4. Información a recopilar Previamente.
   1. Consulte los catálogos generales y es conveniente que cree una copia local de los mismos con los empates apropiados a su base de datos.
   2. Revise las categorías a utilizar, no se llene de información que no lo agregue valor a su proceso.
   3. Revise las comisiones de cada Market, esto le ayudará a definir si desea incluir precios diferenciados por MarketPlace.
   4. Revise las condiciones y las ventajas comerciales que le ofrecen los MarketPlaces, en caso de que desee que algún producto no sea ofertado en algún MarketPlace en particular.
   5. Recopile la información de medidas, peso y UPC de cada producto.
   6. Revise los atributos de la categoría para ver que información adicional requiere.
5. Proceso de alta.
   1. De de alta el producto inicialmente. [(Producto)](../examples/python/productos.py)
   2. Agregue el Stock de cada variación, todos los productos al menos tienen 1 variación, el SkuPadre y el SellerSku, pueden ser el mismo. [(Stock)](../examples/python/stock.py)
   3. Complemente la información de la variación. [(Variación)](../examples/python/variacion.py)
   4. Agregue los precios de cada producto por cada MarketPlace. [(Precios)](../examples/python/precios.py)
   5. Segregue los productos que no desee, de manera predeterminada los productos se publican en todos los Markets. [(Publicar)](../examples/python/publicar.py)
   6. Autorice a MarketSync publicar su catálogo en cada Market [(Markets)](../examples/python/markets.py)
   7. Actualice su stock regularmente y actualice la fecha de actualización de su inventario.
   8. Revise los pedidos e intente enviar dentro de las 24 horas siguientes.


#### También le puede interesar:

- [Servidor](https://github.com/hvalles/marketsync/blob/master/links/server.md)
- [Ruta de Recurso](https://github.com/hvalles/marketsync/blob/master/links/url.md)
- [Conjunto de Llaves](https://github.com/hvalles/marketsync/blob/master/links/keys.md)
