import logging 


logging.basicConfig(
	level=logging.DEBUG,
	filename = "test1.log",
	filemode = 'a',
	format = "%(name)s  :: pid: %(process)d datetime: %(asctime)s level: %(levelname)s message: %(message)s",
	datefmt='%d-%b-%y %H:%M:%S'
	)

""" level: The root logger will be set to the specified severity level.
 filename: This specifies the file.
 filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
 format: This is the format of the log message."""


logging.debug('This is a debug message') #
logging.info('This is an info message') # 
logging.warning('This is a warning message') # WARNING:root:This is a warning message
logging.error('This is an error message') # ERROR:root:This is an error message
logging.critical('This is a critical message') # CRITICAL:root:This is a critical message

""" 
logging provides root logger of python. 
info and debug didn't printed because root logger default severity level is warning.
python logging module didn't follow PEP8 styleguide. Because it is adopted by java's log4j that's why it uses camel casing. 
"""

logging.info(logging.DEBUG) # 10
logging.info(logging.INFO) # 20
logging.info(logging.WARNING) # 30 
logging.info(logging.ERROR) # 40 
logging.info(logging.CRITICAL) # 50

"""The choosen logging level's greater or equal loggers get printed. Ex: if you choose INFO then waning, error and critical get printed. But debug not.
"""
project_name = "Pilgrims"
logging.info("%s Project is running now", project_name)

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
  # or
  logging.exception("Exception occurred")

