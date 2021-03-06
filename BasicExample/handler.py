import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.error('This is an error')