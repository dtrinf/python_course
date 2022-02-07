
# Reto 7


### Starting Postgres as a Docker container
```
docker run -d --rm \
    --name postgres \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=changeme \
    -e PGDATA=/var/lib/postgresql/data/pgdata \
    -v $(pwd):/var/lib/postgresql/data \
    postgres
```

### Conexion inside the contaiener
```
docker exec -it postgres bash
```

### Database and tables creation
```
psql -U admin -d admin -a -f /var/lib/postgresql/data/reto7.sql
```

