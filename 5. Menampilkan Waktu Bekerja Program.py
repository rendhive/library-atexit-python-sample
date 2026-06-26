import atexit
import time

start_time = time.time()

def display_runtime():
    elapsed_time = time.time() - start_time
    print(f"Program berjalan selama {elapsed_time:.2f} detik.")

atexit.register(display_runtime)

# Simulasi program berjalan
print("Program sedang berjalan...")
time.sleep(2)  # Program ditunda selama 2 detik