class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self):
        print("Jenis Kendaraan:", self.jenis)
        print("Kecepatan Maksimum:", self.kecepatan_maksimum, "km/jam")
    
    def bergerak(self):
        return "Kendaraan sedang bergerak"

class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)  # Memanggil konstruktor induk
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        self.info_kendaraan()  # Menampilkan info dari kelas induk
        print("Merk Mobil:", self.merk)
        print("Jumlah Pintu:", self.jumlah_pintu)
    
    def bunyikan_klakson(self):
        return "Tin..tin.."

class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)  # Memanggil konstruktor induk
        self.__tenaga_kuda = tenaga_kuda  # Private attribute
        self.__harga = harga  # Private attribute

    # Getter dan Setter untuk tenaga_kuda
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda

    def set_tenaga_kuda(self, value):
        self.__tenaga_kuda = value

    # Getter dan Setter untuk harga
    def get_harga(self):
        return self.__harga

    def set_harga(self, value):
        self.__harga = value

    def info_mobil_sport(self):
        self.info_mobil()  # Menampilkan info dari kelas Mobil
        print("Tenaga Kuda:", self.__tenaga_kuda, "HP")
        print("Harga:", self.__harga, "juta rupiah")

    def mode_balap(self):
        return "Mobil sport masuk ke mode balap!"

# Contoh Penggunaan
mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 5000)
mobil_sport.info_mobil_sport()

# Menggunakan Getter
print("Tenaga Kuda:", mobil_sport.get_tenaga_kuda())

# Menggunakan Setter
mobil_sport.set_tenaga_kuda(750)
print("Tenaga Kuda setelah update:", mobil_sport.get_tenaga_kuda())

print(mobil_sport.mode_balap())
