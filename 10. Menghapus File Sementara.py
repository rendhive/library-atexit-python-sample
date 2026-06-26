import atexit
import os

temp_file = 'temp.txt'

def remove_temp_file():
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"{temp_file} dihapus.")

atexit.register(remove_temp_file)

with open(temp_file, 'w') as f:
    f.write("Ini file sementara.")
print("File sementara dibuat.")