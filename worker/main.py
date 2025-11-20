from dotenv import load_dotenv

from config.main_config import configuration
from worker_class import Worker

load_dotenv()

def start_worker():
  worker = Worker(configuration)

  is_continue = True
  while is_continue:
    is_continue = worker.start()

  del worker

start_worker()