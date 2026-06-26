import atexit
import datetime

def log_exit_time():
    with open("exit_log.txt", "a") as f:
        f.write(f"Program keluar pada: {datetime.datetime.now()}\n")

atexit.register(log_exit_time)

print("Program sedang berjalan...")