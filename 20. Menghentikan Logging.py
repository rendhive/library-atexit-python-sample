import atexit

logging_enabled = True

def stop_logging():
    global logging_enabled
    logging_enabled = False
    print("Logging dinonaktifkan.")

atexit.register(stop_logging)

print("Program sedang berjalan...")