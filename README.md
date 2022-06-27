##TODOs
- [x] Admin und User Dockern
- [x] URL und Passwörter in .env auslagern
- [ ] RabbitMQ
- [ ] User Datenbank

### Create '.env'-File in each folder (WINDOWS)
```console
cd user
echo > .env
```
```console
cd admin
echo > .env
```

Define enviroment variables (example):

```text
AMPQ_CONNECTION_STRING=amqps://...
MYSQL_DATABASE=main
MYSQL_USER=admin
MYSQL_PASSWORD=admin
MYSQL_ROOT_PASSWORD=root
DB_CONNECTION_STRING=mysql://admin:admin@db/main
```

### Build container with
```console
...WK_2608_EVA\admin:~$ docker-compose build
...WK_2608_EVA\user:~$ docker-compose build
```

### Start container with
```console
docker-compose up
```

**Notice:** The 'backend' container depends on 'db' container!
Sometimes it may take a bit longer...

---

### Dependencies
**User**
```console
Flask==2.1.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
pika==1.2.1
SQLAlchemy==1.4.39
mysqlclient==2.1.0
requests==2.28.0
python-dotenv==0.20.0
```

**Admin**
```console
Flask==2.1.2
Flask-SQLAlchemy==2.5.1
Flask-WTF==1.0.1
pika==1.2.1
SQLAlchemy==1.4.39
mysqlclient==2.1.0
python-dotenv==0.20.0
```