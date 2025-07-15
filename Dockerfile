FROM python:3.11

RUN apt-get update
RUN pip install "fastapi[standard]"
RUN pip install python-dotenv Werkzeug 
RUN pip install requests uvicorn motor pydantic
WORKDIR /users
COPY users /users

CMD ["fastapi", "run", "main.py", "--port", "8000", "--reload"]
