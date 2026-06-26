import atexit

def check_connection_status():
    print("Koneksi telah diperiksa.")

atexit.register(check_connection_status)

print("Program sedang berjalan...")