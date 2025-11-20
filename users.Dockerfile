FROM python:3.11

RUN apt-get update
RUN pip install "fastapi[standard]"
RUN pip install python-dotenv Werkzeug 
RUN pip install requests uvicorn motor pydantic
RUN pip install fastapi-sqlalchemy
RUN pip install mysqlclient
RUN pip install alembic
WORKDIR /users
COPY users /users

CMD ["fastapi", "run", "main.py", "--port", "8000", "--reload"]
