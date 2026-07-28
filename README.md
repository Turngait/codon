# Codon Project

## API of Codon project  
This project is an open-source based. Every can use this code or join to development of the project.


### About modules
- Soma module - all about state of body and mind: temperature, weight, heart rhythm, symptoms, illnesses, etc
- Homoeostasis module - personal analysis, etc
- Consumption module - about food, medicines, sports, etc

### Links:
- Client https://github.com/Turngait/codon_client_web
- API https://github.com/Turngait/codon
- UX https://www.figma.com/board/dc6DPCRqNgvn49ngdIjmHW/UX-Codon?node-id=0-1&t=onUWEmkwWGvRekuS-1
- UI https://www.figma.com/design/kuMJTvdEXLHONp9LwcufTM/Codon?node-id=26-2&t=0yY1h7dGG5w2eLLS-1

### Requirements
You need to install this application:
```
git
nodejs
npm
docker
docker-compose
```

### Local project set up
1. Make that commds:
```
git clone URL api
cd api/auth
npm install
cd ../gate
npm install
cd ..
cp .env.example .env
```

2. After you need to create DB
```
docker compose -f docker-compose.db.yaml up
```

3. Go to http://localhost:8087/ and create `users` DB and `users_data` DB

4. Go to http://localhost:8086/ and crete `codon` and `codon_health` DBs

5. And now you need to create mongo user
	Go to Mongo's container. Login and Password you need to add to .env file
```
docker exec -it cd-mongo-codon bash

mongosh -U ROOT_LOGIN(login and password in env file)

use codon

db.createUser({user: "LOGIN", pwd: "PASSWORD",roles: [ { role: "readWrite", db: "codon" }]})

exit
```

6. And now you are ready to lunch local app
```
docker compose up
```

### Running the API

```bash
# local development

$ docker-compose up
```

## This project developed by
https://github.com/Turngait
