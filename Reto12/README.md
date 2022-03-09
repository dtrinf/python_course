

```
docker run -d --rm \
    --name postgres \ 
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=changeme \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v $(pwd):/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

Conectarse al container de Docker, y cargar los datos

(También es posible hacerlo externamente si se tiene instalado psql)

```
docker exec -it postgres bash

psql -U admin -d admin -a -f /var/lib/postgresql/data/dump/reto12.sql
```

Creamos el usuario Django y le damos privilegios para usar la bbdd importada
Si creamos el usuario con otra contraseña, es necesario modificar la conexión en la configuración del projecto de Django
(reto12/reto12/settings.py)

```
psql -U admin 

CREATE USER djangouser WITH ENCRYPTED PASSWORD 'djangopass';

ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE reto12 TO djangouser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO djangouser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO djangouser;

\q
```

Ahora es necesario instalar los requerimientos de Django para ejecutar el proyecto

```
pip install -r requirements.txt
```

Una vez instalados, podemos ejecutar la web

```
python reto12/manage.py runserver
```


http://127.0.0.1:8000/

http://127.0.0.1:8000/api/v1/rest-auth/registration
http://127.0.0.1:8000/api/v1/rest-auth/login
http://127.0.0.1:8000/api/v1/rest-auth/logout
http://127.0.0.1:8000/books/