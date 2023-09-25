from pathlib import Path
import pytest
from datetime import datetime
from heartbeat.my_log import logger

filename = Path(__file__).parent / "hblog"

log_files = [filename]


def seconds_difference(Timestamp1, Timestamp2):
    # Convert the time strings to datetime objects
    time_format = "%H:%M:%S"  # The format of your time strings
    time1 = datetime.strptime(Timestamp1, time_format)
    time2 = datetime.strptime(Timestamp2, time_format)
    # Calculate the time difference in seconds
    time_difference_seconds = (time2 - time1).total_seconds()

    return time_difference_seconds


@pytest.mark.parametrize("file_be_parsed", log_files)
def test_check_log_time_difference(file_be_parsed):
    for file in log_files:
        with open(file, mode="r") as f:
            lines = f.readlines()
            # reverse the lines for comfort
            reversed_lines = lines[::-1]
            Timestamp1 = reversed_lines[0].split()[10]
            for line in reversed_lines[1:]:
                Timestamp2 = line.split()[10]
                time_diff = seconds_difference(Timestamp1, Timestamp2)
                if 30 < time_diff < 32:
                    logger.warning(f"Time difference is {time_diff} seconds")
                elif time_diff >= 32:
                    logger.error(f"Time difference is {time_diff} seconds")
                Timestamp1 = Timestamp2


if __name__ == "__main__":
    test_check_log_time_difference(log_files)
