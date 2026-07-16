# Codon API
API of Codon project

Documentation:
```
https://ilya-ry.atlassian.net/wiki/spaces/MieliBioLa/pages/28246017/Codon+Project
```

This project is an open-source based. Every can use this code or join to development of the project.

## Requirements
You need to install this application:
```
git
nodejs
npm
docker
docker-compose
```


## Local project set up
```
git clone URL api
cd api/auth
npm install
cd ../gate
npm install
cd ..
cp .env.example .env
```

After you need to create DB
```
docker compose -f docker-compose.db.yaml up
```
Go to http://localhost:8087/ and create `users` DB and `users_data` DB
Go to http://localhost:8086/ and crete `codon` and `codon_health` DBs

And now you need to create mongo user
Go to Mongo's container
```
docker exec -it cd-mongo-codon bash

mongo -U ROOT_LOGIN(login and password in env file)
use codon
db.createUser({user: "operator2", pwd: "adm123",roles: [ { role: "readWrite", db: "codon" }]})
exit

```

And now you are ready to lunch local app

## Running the app

```bash
# local development
$ docker-compose up
```
### This project developed by
```
http://ilya-r.com/
```