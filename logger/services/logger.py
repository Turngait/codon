import logging

def logger(msg: str, level: str = "INFO") -> bool:
  try:
    logLevel = logging.ERROR if level == "ERROR" else logging.INFO
    logging.basicConfig(level=logLevel, filename="logs.log",filemode="w")
    logging.info(msg)
    return True
  except BaseException as err:
    print(err)
    return False
