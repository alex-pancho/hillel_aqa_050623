import re
import logging

# Homework for lesson 23
"""
Моніторингова система клєнта надсилає сигнал кожні 30 сек.
Засобами автоматизації проаналізуйте наданий нам лог в папці heartbeat\hblog.
Змініть заготовку - файл hb_proces.py так? щоб там був аналіз правилності вимоги:
для кожного випадку де hertbeat більше 30 сек але менше 32 логувало варнінг в файл log_file.log
для кожного випадку де hertbeat більше рівно 32 логувало error в файлік log_file.log
Необовязова частина, виклик для найтриваліших: (на оцінку не впливає, на самоцінку - впливає) Врахуйте, що завтра вам використовувати файл hb_proces.py для тестів багатьох файлів
Здається через посилання на PR з змінами одного файлу (hb_proces.py), АЛЕ додатково приатачте у форму відповіді лог, що сворить ваша робота.
ЛОГ в PR потрапити НЕ ПОВИНЕН.
"""

# Configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler for logging to a file
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler for logging to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Set the log message format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Open the log file for reading
with open("hblog", "r") as logfile:
    lines = logfile.readlines()

# Open the log file for writing
with open("log_file.log", "w") as log_file:
    for line in lines:
        # Find the timestamp using regular expressions
        match = re.search(r'Timestamp (\d+:\d+:\d+)', line)

        if match:
            timestamp_str = match.group(1)
            hours, minutes, seconds = map(int, timestamp_str.split(':'))
            seconds_since_midnight = hours * 3600 + minutes * 60 + seconds

            if 30 < seconds_since_midnight <= 32:
                log_file.write(f"Warning: Timestamp is {timestamp_str}, but it should be within 30 seconds.\n")
                logger.warning(f"Timestamp is {timestamp_str}, but it should be within 30 seconds.")
            elif seconds_since_midnight > 32:
                log_file.write(f"Error: Timestamp is {timestamp_str}, which is not acceptable.\n")
                logger.error(f"Timestamp is {timestamp_str}, which is not acceptable.")

# Log the completion of the analysis
logger.info("Heartbeat log analysis completed.")
