"""
HomeWork_23Моніторингова система клєнта надсилає сигнал кожні 30 сек.
Засобами автоматизації проаналізуйте наданий нам лог в папці heartbeat\hblog.
Змініть заготовку - файл hb_proces.py так? щоб там був аналіз правилності вимоги:
1. для кожного випадку де hertbeat більше 30 сек але менше 32 логувало варнінг в файл log_file.log
2. для кожного випадку де hertbeat більше рівно 32 логувало error в файлік log_file.log
"""

from pathlib import Path
import re
from logger import logger
from datetime import datetime, timedelta

# Паттерн для поиска временной метки в строке
timestamp_pattern = r"(\d{2}:\d{2}:\d{2})"
# Объявляем переменную для предыдущей временной метки
previous_timestamp = None

filename = Path(__file__).parent / "hblog"
print(filename)

with open(filename, mode="r") as f:
    for line in f:
        # Извлекаем временную метку из строки
        match = re.search(timestamp_pattern, line)
        if match:
            timestamp = match.group(1)
            # Преобразуем временную метку из формата строки в формат времени
            current_timestamp = datetime.strptime(timestamp, "%H:%M:%S")
            # print(current_timestamp)
             # Проверка, что у нас есть предыдущая временная метка
            if previous_timestamp is not None:
                # Рассчитываем разницу во времени между текущей и предыдущей метками
                time_difference = previous_timestamp - current_timestamp
                # Проверяем, что разница находится в интервале от 30 до 32 секунд и логируем варнинг
                if timedelta(seconds=30) < time_difference < timedelta(seconds=32):
                    logger.warning(f"Timestamp = {previous_timestamp.strftime('%H:%M:%S')}, heartbeat = {time_difference} sec")
                # Проверяем, что разница больше 32 секунд и логируем Еррор
                elif timedelta(seconds=32) <= time_difference:
                    logger.error(f"  Timestamp = {previous_timestamp.strftime('%H:%M:%S')}, heartbeat = {time_difference} sec")
            # Обновляем предыдущую временную метку
            previous_timestamp = current_timestamp
