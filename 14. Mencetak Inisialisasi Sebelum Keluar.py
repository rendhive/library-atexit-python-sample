import atexit

def before_exit():
    print("Inisialisasi sebelum keluar...")

atexit.register(before_exit)

print("Program sedang berjalan...")