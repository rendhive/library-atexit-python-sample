import atexit

def global_cleanup():
    print("Pembersihan global dilakukan.")

atexit.register(global_cleanup)

print("Program telah selesai.")