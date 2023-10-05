r"""HomeTask_23.

Моніторингова система клєнта надсилає сигнал кожні 30 сек.
Засобами автоматизації проаналізуйте наданий нам лог в папці heartbeat\hblog.
https://github.com/alex-pancho/hillel_aqa_050623/blob/main/heartbeat/hblog
Змініть заготовку - файл hb_proces.py так, щоб там був
аналіз правильності вимоги.
для кожного випадку де hertbeat більше 30 сек але менше
32 логувало варнінг в файл log_file.log
для кожного випадку де hertbeat більше рівно 32 логувало
error в файлік log_file.log
"""
import re
import time

timestamp_pattern = r'Timestamp (\d+:\d+:\d+)'

log_file_path = 'hblog'

output_log_path = 'log_file.log'

min_interval = 30
max_interval = 32

with open(log_file_path, 'r') as log_file, open(output_log_path, 'a') as output_log_file:
    for line in log_file:
        timestamp_match = re.search(timestamp_pattern, line)
        if timestamp_match:
            timestamp_str = timestamp_match.group(1)
            timestamp = time.strptime(timestamp_str, '%H:%M:%S')
            seconds_since_midnight = timestamp.tm_hour * 3600 + timestamp.tm_min * 60 + timestamp.tm_sec
            if seconds_since_midnight > min_interval and seconds_since_midnight <= max_interval:
                output_log_file.write(f'Warning: {line}')
            elif seconds_since_midnight > max_interval:
                output_log_file.write(f'Error: {line}')

log_file.close()
output_log_file.close()
