from pathlib import Path
from datetime import datetime


def parse_log_file(input_file_path, output_file_path):
    """
    Parse an input log file and write warnings or errors to an output log file based on time differences.
    args:
        input_file_path (str or Path): The path to the input log file to be parsed.
        output_file_path (str or Path): The path to the output log file where warnings or errors will be written.
    return: None
    """
    last_signal_time = {}

    try:
        with open(input_file_path, mode="r") as f, open(output_file_path, mode="a") as log_file:
            for line in f.readlines():
                parts = line.split()
                if len(parts) >= 12:
                    key = parts[12]
                    timestamp = parts[10]

                    try:
                        signal_time = datetime.strptime(timestamp, "%H:%M:%S")
                    except ValueError:
                        continue

                    if key in last_signal_time:
                        time_difference = (last_signal_time[key] - signal_time).seconds

                        if 30 < time_difference < 32:
                            log_file.write(
                                f"Warning: For Key {key} time is {time_difference}s between "
                                f"{signal_time.strftime('%H:%M:%S')} - {last_signal_time[key].strftime('%H:%M:%S')}.\n")
                        elif time_difference >= 32:
                            log_file.write(
                                f"Error: For Key {key} time is {time_difference} s between "
                                f"{signal_time.strftime('%H:%M:%S')} - {last_signal_time[key].strftime('%H:%M:%S')}.\n")

                    last_signal_time[key] = signal_time

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    log_file_path = Path(__file__).parent / "hblog"
    output_log_path = Path(__file__).parent / "log_file.log"

    parse_log_file(log_file_path, output_log_path)
