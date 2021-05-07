# Marketsync Documentación de API 
### Seccion del conjunto de llaves

[Inicio](/)

### Descripción de las llaves

##### Llave pública
La llave pública se le conoce como el token y sirve para identificar el origen de la petición, de que usuario corresponde y por lo tanto de que empresa o cliente le pertenece, usualmente esta compuesta por un hash de entre 30 y 40 caracteres y se incluye 
en todas las peticiones realizadas.

```http
    ?token=dsfkdskf4390534dksfmnsdfnm
```

##### Llave privada
La llave privada de genera en la sección de usuarios, ->Ver Opciones -> Mis usuarios -> Reset Private Key, este hash, nho deberá de ser compartido con otros usuarios y en caso de creer que el mismo se encuentra comprometido, debera de resetearlo; para obtener uno nuevo.

El hash se utiliza como token de encriptación al momento de firmar la petición e incluir el parámetro signature con el resultado del mismo.

```http
    ?signature=dsfkdskf4390534dksfmnsdfnm
```

### Generación de Firma

#### Versión Python 2.7
```python

import requests # Librería externa debe instalar -> pip install requests
import urllib
from datetime import datetime, timedelta
import hashlib
from hmac import HMAC

PRIVATE_KEY = 'YOUR PRIVATE KEY HERE'
TOKEN = 'YOUR PUBLIC TOKEN HERE'
SERVER = 'URL FOR MARKETSYNC SERVER ASSIGNED'

# Set initial parameters
parameters = {}
parameters['token'] = TOKEN
parameters['timestamp'] = str(datetime.now().isoformat()) # YYYY-MM-DDTHH:mm:ss
parameters['version'] = '1.0'

# You may add others parameters here
# ...

# Signature parameter should not be included 
concatenated = str(urllib.urlencode(sorted(parameters.items())))

sign = HMAC(PRIVATE_KEY, concatenated, hashlib.sha256).hexdigest()
# Reemplace controller con el controlador deseado.
url = SERVER + 'controller?' + concatenated + '&signature=' + sign
print url
r = requests.get(url)
for x in r.json().get('answer',[]):
    print x


```

#### Versión PHP 7+
```PHP

$PRIVATE_KEY = 'YOUR PRIVATE KEY HERE'
$TOKEN = 'YOUR PUBLIC TOKEN HERE'
$SERVER = 'URL FOR MARKETSYNC SERVER ASSIGNED'

# Set initial parameters
$parameters = [];
$parameters['token'] = $TOKEN;
$parameters['timestamp'] = substr(date(DATE_ATOM),0,19); # YYYY-MM-DDTHH:mm:ss
$parameters['version'] = '1.0';
        
# You may add others parameters here
# ...

ksort($parameters);
// URL encode the parameters.
$encoded = array();
foreach ($parameters as $name => $value) {
    $encoded[] = rawurlencode($name) . '=' . rawurlencode($value);
}
// Concatenate the sorted and URL encoded parameters into a string.
$concatenated = implode('&', $encoded);

$sign = rawurlencode(hash_hmac('sha256', $concatenated, $PRIVATE_KEY, false));
# Reemplace controller con el controlador deseado.
$url = $SERVER . 'controller?' . $concatenated . '&signature=' . $sign;

// HACER LLAMADO CURL


```
[Ver llamada CURL en PHP] (https://www.php.net/manual/es/curl.examples-basic.php)

> :information_source: Importante
> El texto controller de las urls expuestas en las llamadas de arriba, debe de ser cambiado por el controlador deseado. ver la sección de controladores para más información.
- [Controladores](/links/controller.html)