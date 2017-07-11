import logging

class WeLogger(object):
  logger = None

  def __init__(self, level):
    if WeLogger.logger is None:
      if level == 'debug':
        self.level = logging.DEBUG
      elif level == 'info':
        self.level = logging.INFO
      elif level == 'warn':
        self.level = logging.WARNING
      elif level == 'error':
        self.level = logging.ERROR
      elif level == 'critical':
        self.level = logging.CRITICAL

      WeLogger.logger = logging.getLogger()
      WeLogger.logger.setLevel(self.level)
      formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(levelname)s : %(message)s')
      ch = logging.StreamHandler()
      ch.setLevel(self.level)
      ch.setFormatter(formatter)
      fh = logging.FileHandler('sync-data.log')
      fh.setLevel(self.level)
      fh.setFormatter(formatter)
      WeLogger.logger.addHandler(ch)
      WeLogger.logger.addHandler(fh)

  def build(self):
    return WeLogger.logger
