# Controle de Estoque

### Criqação de um projeto Flask com Docker:

```sh
docker-compose build --no-cache
docker-compose up --build -d 
```

### Criação de estrutura de diretórios:

```sh
docker exec -it estoque-flask ls /app
docker exec -it estoque-flask python /app/setup_project.py
```

### Teste do ORM SQLAlchemy:

```sh
docker exec -it estoque-flask python /app/testeSQLAlchemy.py
```

### Teste de conexão com o banco de dados:

```sh
docker-compose exec flask-src python test_db_connection.py
```

### Criação de tabelas no banco de dados:

```sh
docker-compose exec flask-src flask db init
docker-compose exec flask-src flask db migrate -m "Create products table"
docker-compose exec flask-src flask db upgrade
```

### Combo de comandos:

```sh
docker-compose down -v 
docker-compose build --no-cache
docker-compose up --build -d 
``` 
