import atexit

def cleanup():
    print("Membersihkan sumber daya...")

atexit.register(cleanup)

print("Program sedang berjalan...")
# Fungsi: Menetapkan fungsi untuk mengelola pembersihan sumber daya.
# Kondisi: Ketika Anda memiliki koneksi atau sumber daya yang perlu dibersihkan sebelum keluar.