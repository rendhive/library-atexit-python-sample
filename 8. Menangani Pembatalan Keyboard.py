import atexit
import signal

def handle_exit(signal, frame):
    print("Keluar dari program.")

signal.signal(signal.SIGINT, handle_exit)
atexit.register(handle_exit)

print("Tekan Ctrl+C untuk keluar.")
# Fungsi: Mengatur fungsi untuk menangani sinyal keluar dari terminal.
# Kondisi: Ketika Anda perlu menyempurnakan logika saat pengguna keluar dengan Ctrl+C.