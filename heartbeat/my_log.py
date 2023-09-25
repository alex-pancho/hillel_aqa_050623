import logging

format_style = '%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s'
# Set the default logging level to DEBUG
logging.basicConfig(level=logging.DEBUG, format=format_style,
                    filename='log_file.log', filemode='w', force=True)

# Create a logger
logger = logging.getLogger(__name__)

# Create a console handler and set its level to DEBUG
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and attach it to the console handler
console_formatter = logging.Formatter(format_style)
console_handler.setFormatter(console_formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

