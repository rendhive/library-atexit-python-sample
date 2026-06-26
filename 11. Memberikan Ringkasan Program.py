import atexit

def summarize():
    print("Program selesai. Terima kasih telah menggunakan.")

atexit.register(summarize)

print("Program sedang berjalan...")