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
docker exec -it estoque-flask python /app/analise.py
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

### 1º Combo de Limpeza e construção:

```sh
docker-compose down -v 
docker-compose build --no-cache
docker-compose up --build -d 
``` 

### 2º Combo de Limpeza e construção:

```sh
docker stop $(docker ps -aq)
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -q)
docker volume prune -f
docker volume rm devopsteste_db-data -f
docker network prune -f
docker system prune -a
``` 
