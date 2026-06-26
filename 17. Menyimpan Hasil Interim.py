import atexit

results = []

def save_results():
    print("Menyimpan hasil interim:", results)

atexit.register(save_results)

results.append("Hasil 1")
results.append("Hasil 2")
print("Hasil interim ditambahkan.")