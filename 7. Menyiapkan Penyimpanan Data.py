import atexit

def save_data():
    print("Data disimpan ke database.")

atexit.register(save_data)

# Simulasi program dengan penyimpanan data
print("Program sedang menjalankan operasi...")