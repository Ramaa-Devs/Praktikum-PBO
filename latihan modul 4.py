# Definisi kelas AkarKuadrat
class AkarKuadrat:
    def __init__(self):
        pass  # Konstruktor, tapi tidak perlu inisialisasi variabel apa pun
    # Metode utama untuk menjalankan program
    def jalankan(self):
        while True:  # Loop terus sampai input valid dan hasil ditampilkan
            try:
                # Meminta input dari pengguna
                input_angka = input("Masukin angka: ")
                # Mengubah input string menjadi float (agar bisa menerima desimal juga)
                angka = float(input_angka)
                # Mengecek apakah angka negatif atau sama dgn 0
                if angka < 0:
                    print("Input tidak valid. Masukin angka positif.")
                elif angka == 0:
                    print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
                else:
                    hasil = angka ** 0.5
                    # Menampilkan hasil perhitungan
                    print(f"Akar kuadrat dari {angka} adalah {hasil}")
                    break# Keluar dari loop 

            # Menangkap error jika input tidak bisa diubah menjadi angka (float)
            except ValueError:
                print("Input tidak valid. Masuin angka yang valid.")

# Membuat objek dari kelas AkarKuadrat
program = AkarKuadrat()

# Menjalankan metode jalankan() untuk memulai program
program.jalankan()
