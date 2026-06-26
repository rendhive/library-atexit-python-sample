import atexit

def goodbye():
    print("Program akan keluar. Selamat tinggal!")

atexit.register(goodbye)

print("Program sedang berjalan...")
# Fungsi: Mengikat fungsi goodbye() untuk dijalankan saat program selesai.
# Kondisi: Ketika Anda ingin menampilkan pesan sebelum program selesai.