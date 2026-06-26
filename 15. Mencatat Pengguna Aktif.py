import atexit

active_users = []

def log_user(activity):
    active_users.append(activity)
    print(f"Pengguna aktif: {activity}")

atexit.register(lambda: print(f"Pengguna aktif saat keluar: {active_users}"))

log_user("User1")
log_user("User2")
# Fungsi: Mencatat pengguna yang aktif saat menjalankan program.
# Kondisi: Ketika Anda ingin tahu pengguna yang berinteraksi dengan aplikasi sebelum keluar.