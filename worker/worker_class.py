import time
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from models.tokens_model import TokensModel


class Base(DeclarativeBase):
    pass


class Worker:
  def __init__(self, config):
    self.config = config
    engine = create_engine(self.config['db']["mysql_users"])
    Session = sessionmaker(bind=engine)
    self.session = Session()
    self.start_time = time.perf_counter()
    print(f'Worker starts at {datetime.now()}')

  def __del__(self):
    print(f'Worker dies. Elapsed time {(time.perf_counter() - self.start_time):.6f} seconds at {datetime.now()}')
    self.session.close()

  def start(self) -> bool:
    self.__wait()
    is_continue_needed = self.__check_tokens()
    return is_continue_needed
    
    
  def __check_tokens(self) -> bool:
    try:
      self.session.query(TokensModel).where(TokensModel.createdAt >= TokensModel.active_til).delete()
      self.session.commit()

    except BaseException as err:
      print(err)
    print(f'Tokens check completed at {datetime.now()}')
    return False
  
  def __wait(self):
    time.sleep(self.config['app']['main_sleep_time'])

