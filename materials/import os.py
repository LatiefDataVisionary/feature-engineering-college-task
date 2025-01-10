import os

# Lokasi folder lama dan nama baru
old_path = r"C:\Users\Halo"
new_path = r"C:\Users\Latief"  # Ganti "NamaAnda" dengan nama Anda

# Mengubah nama folder
try:
    os.rename(old_path, new_path)
    print(f"Folder berhasil diubah menjadi: {new_path}")
except FileNotFoundError:
    print(f"Folder {old_path} tidak ditemukan.")
except PermissionError:
    print("Tidak memiliki izin untuk mengubah nama folder.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
