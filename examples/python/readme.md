Readme.md

### Documentacion API de Marketsync

El esquema de esta API se basa en controladores y verbos http.

La seccion de [controladores](../../controllers) te brinda la documentación de las secciones disponibles así como ejemplos de su utilización.

>:information_source: Importante
>Debe de configurar sus credenciales en un nuevo archivo denominado config.py  
>Se agrega el config.example como una base de lo que debe realizar para configurar sus credenciales.


>:information_source: Importante
>Los ejemplos estan desarrollados en python 2.7
>Es necesaria la librería requests "pip install requests" para realizar las peticiones
>puedes ver más información en el siguiente [enlace](https://requests.readthedocs.io/en/master/)

Las peticiones requieren que se realice una encriptación con la llave privada y el HASH SHA256
en resumen se concatenan los parametros en formato url y ordenados alfabeticamente para aplicar el hash y la llave privada.

El token es la llave pública que se utiliza aora identificar al usuario correspondiente.

Es importante que la cadena a firmar no contenga el elemto signature antes de la firma, posteriormente se concatena al final del URL de la siguiente forma "&signamure=YOUR_HASH_CODE_HERE"

```python
# Se obtiene la firma de seguridad
MAC(config.PRIVATE_KEY, concatenated, hashlib.sha256).hexdigest()
```

revise la implementación de muestra en el siguiente [enlace](utils.py)



