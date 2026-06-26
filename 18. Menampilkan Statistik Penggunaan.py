import atexit

usage_count = 0

def show_usage_statistics():
    print(f"Program telah dijalankan {usage_count} kali.")

atexit.register(show_usage_statistics)

usage_count += 1
print("Program sedang berjalan.")