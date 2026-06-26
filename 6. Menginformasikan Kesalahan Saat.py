import atexit

def report_error():
    print("Ada kesalahan saat menjalankan program.")

atexit.register(report_error)

# Simulasi program dengan kesalahan
print("Program sedang berjalan...")
raise Exception("Simulated Exception")  # Menyebabkan program berhenti