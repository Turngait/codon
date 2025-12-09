FROM python:3.11

RUN apt-get update
RUN pip install python-dotenv Flask Werkzeug
RUN pip install -U flask-cors
RUN pip install requests
WORKDIR /logger
COPY logger /logger

CMD ["python", "main.py"]