import atexit

def notify_exit():
    print("Program telah selesai dengan sukses.")

atexit.register(notify_exit)

print("Program untuk melakukan tugas.")
# Simulasi beberapa tugas