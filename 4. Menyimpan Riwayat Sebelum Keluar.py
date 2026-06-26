import atexit

history = []

def save_history():
    with open('history.txt', 'w') as f:
        for item in history:
            f.write(f"{item}\n")
    print("Riwayat disimpan.")

atexit.register(save_history)

history.append("Input 1")
history.append("Input 2")
# Fungsi: Menyimpan riwayat pengguna ke dalam file saat program keluar.
# Kondisi: Ketika Anda ingin menyimpan status pengguna sebelum aplikasi ditutup.