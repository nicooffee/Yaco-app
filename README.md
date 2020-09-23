# Introducción
  Yaco es una aplicación web escrita en Python (Flask) de aprendizaje de vocabulario inglés para hispanohablantes. La información de vocabulario utilizada es provista por la [Merriam-Webster's Spanish-English API](https://dictionaryapi.com/products/api-spanish-dictionary) y el funcionamiento del sistema está basado en las técnicas [SRS](https://en.wikipedia.org/wiki/Spaced_repetition) y [Flashcard](https://en.wikipedia.org/wiki/Flashcard).
# Requerimientos
Para ejecutar la aplicación son necesarias las siguientes herramientas/servicios: 
1.	API key de [Merriam-Webster's Spanish-English API](https://dictionaryapi.com/products/api-spanish-dictionary).
2.	Servidor [PostgreSQL](postgresql.com) 9.6+.
3.	Python 3.6.x
4.  Ubuntu 18.04

# Instalación
Para ejecutar Yaco se deben preparar todas las herramientas que utiliza. En las siguiente subsecciones se detalla cómo preparar cada una.
## Base de datos
En el servidor, crear dos bases de datos, una con el nombre de `yaco` y la otra con el nombre de `sessions`. En la base de datos `yaco`, ejecutar el script que se encuentra en el archivo `/bdd/yaco_tablas.sql`, el cual creará todas las tablas que requiere yaco.

Antes de crear las tablas de la  base de datos `sessions`, crear el archivo `/yaco/DatabaseData.py` y escribir el siguiente código dentro de él (con los datos correspondientes a las bases de datos recién creadas).
```python
  user = "<DATABASE_USER>"
  host = "<HOST_IP>"
  port = "<SERVER_PORT>"
  db_model_name = "yaco" 
  db_model_pswd = "<YACO_PASSWORD>"
  db_sess_name = "sessions"
  db_sess_pswd = "<SESSIONS_PASSWORD>"
```
Una vez creado el archivo, dentro de `/yaco`, ejecutamos `python3` en la consola y ejecutamos las siguientes líneas de código:
```python
  from app import sess
  sess.app.session_interface.db.create_all()
```
Luego de esa operación, las tablas de la base de datos `sessions` serán creadas.
## API KEY
Luego de obtener la API key del diccionario, reemplazar el valor de `API_KEY` del archivo `/yaco/class/config/config.py`
```python
  API_KEY = "<YOUR_API_KEY>"
```
## Python
En el directorio `/yaco`, instalar las dependencias que utiliza la aplicación para funcionar. Esto se hace desde la consola de Linux con el comando:
```bash
  pip3 install -r requirements.txt
```
Finalmente, Yaco está listo para ser ejecutado, lo cual puede ser realizado con el script `/yaco/cmp.sh`. Para ejecutar el script realizamos:
```bash
  bash cmp.sh
```
Con esto, la aplicación funciona en el link provisto en la consola.
