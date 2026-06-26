import atexit

configuration = {'option': 'value', 'setting': 'enabled'}

def clear_config():
    configuration.clear()
    print("Konfigurasi dihapus.")

atexit.register(clear_config)

print("Program sedang berjalan...")