from testYaml import logger

logger.debug('This is a debug message') #
logger.info('This is an info message') # 
logger.warning('This is a warning message') # WARNING:root:This is a warning message
logger.error('This is an error message') # ERROR:root:This is an error message
logger.critical('This is a critical message') # CRITICAL:root:This is a critical message

project_name = "Pilgrims"
logger.info("%s Project is running now", project_name)

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logger.exception("Exception occurred")