FROM python:3.11

RUN apt-get update
RUN pip install python-dotenv 
RUN pip install requests
RUN pip install sqlalchemy
RUN pip install mysqlclient
WORKDIR /worker
COPY worker /worker

CMD ["python3", "main.py"]
