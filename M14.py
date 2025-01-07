class BaseData:
    def __init__(self):
        self.id = None
        self.nama = None
    
    def display_info(self):
        pass

class Dosen(BaseData):
    def __init__(self, id, nama):
        super().__init__()
        self.id = id
        self.nama = nama
    
    def display_info(self):
        return f"Dosen - ID: {self.id}, Nama: {self.nama}"

class Matakuliah(BaseData):
    def __init__(self, kode, nama):
        super().__init__()
        self.id = kode
        self.nama = nama
    
    def display_info(self):
        return f"Matakuliah - Kode: {self.id}, Nama: {self.nama}"

class Mahasiswa(BaseData):
    def __init__(self, nim, nama):
        super().__init__()
        self.id = nim
        self.nama = nama
        self.status = "Aktif"
    
    def display_info(self):
        return f"Mahasiswa - NIM: {self.id}, Nama: {self.nama}, Status: {self.status}"

class Perkuliahan:
    def __init__(self, id, id_dosen, kode_mk, waktu):
        self.id = id
        self.id_dosen = id_dosen
        self.kode_mk = kode_mk
        self.waktu = waktu
    
    def display_info(self):
        return f"Perkuliahan - ID: {self.id}, ID Dosen: {self.id_dosen}, Kode MK: {self.kode_mk}, Waktu: {self.waktu}"

class Kampus:
    def __init__(self):
        self.dosen_list = {}
        self.matakuliah_list = {}
        self.mahasiswa_list = {}
        self.perkuliahan_list = {}
    
    def tambah_dosen(self, id, nama):
        if id in self.dosen_list:
            raise ValueError("Dosen dengan ID tersebut sudah ada")
        dosen = Dosen(id, nama)
        self.dosen_list[id] = dosen
        return dosen.display_info()
    
    def tambah_matakuliah(self, kode, nama):
        if kode in self.matakuliah_list:
            raise ValueError("Matakuliah dengan kode tersebut sudah ada")
        mk = Matakuliah(kode, nama)
        self.matakuliah_list[kode] = mk
        return mk.display_info()
    
    def tambah_mahasiswa(self, nim, nama):
        if nim in self.mahasiswa_list:
            raise ValueError("Mahasiswa dengan NIM tersebut sudah ada")
        mhs = Mahasiswa(nim, nama)
        self.mahasiswa_list[nim] = mhs
        return mhs.display_info()
    
    def tambah_perkuliahan(self, id, id_dosen, kode_mk, waktu):
        if id in self.perkuliahan_list:
            raise ValueError("Perkuliahan dengan ID tersebut sudah ada")
        if id_dosen not in self.dosen_list:
            raise ValueError("Dosen tidak ditemukan")
        if kode_mk not in self.matakuliah_list:
            raise ValueError("Matakuliah tidak ditemukan")
        if len(self.mahasiswa_list) == 0:
            raise ValueError("Belum ada mahasiswa yang terdaftar")
            
        perkuliahan = Perkuliahan(id, id_dosen, kode_mk, waktu)
        self.perkuliahan_list[id] = perkuliahan
        return perkuliahan.display_info()
    
    def detail_dosen(self, id):
        if id not in self.dosen_list:
            raise ValueError("Dosen tidak ditemukan")
        return self.dosen_list[id].display_info()
    
    def detail_matakuliah(self, kode):
        if kode not in self.matakuliah_list:
            raise ValueError("Matakuliah tidak ditemukan")
        return self.matakuliah_list[kode].display_info()
    
    def detail_mahasiswa(self, nim):
        if nim not in self.mahasiswa_list:
            raise ValueError("Mahasiswa tidak ditemukan")
        return self.mahasiswa_list[nim].display_info()
    
    def detail_perkuliahan(self, id):
        if id not in self.perkuliahan_list:
            raise ValueError("Perkuliahan tidak ditemukan")
        return self.perkuliahan_list[id].display_info()

if __name__ == "__main__":
    kampus = Kampus()
    
    while True:
        print("\n=== SISTEM MANAJEMEN DATA KAMPUS ===")
        print("1. Manajemen Dosen")
        print("2. Manajemen Matakuliah")
        print("3. Manajemen Mahasiswa")
        print("4. Manajemen Perkuliahan")
        print("0. Keluar")
        
        pilihan = input("\nMasukkan pilihan menu (0-4): ")
        
        if pilihan == "0":
            print("Terima kasih telah menggunakan sistem ini!")
            break
            
        elif pilihan == "1":
            while True:
                print("\n=== MANAJEMEN DOSEN ===")
                print("1. Tambah Dosen")
                print("2. Lihat Detail Dosen")
                print("0. Kembali ke Menu Utama")
                
                sub_pilihan = input("\nMasukkan pilihan (0-2): ")
                
                if sub_pilihan == "0":
                    break
                elif sub_pilihan == "1":
                    id_dosen = input("Masukkan ID Dosen: ")
                    nama_dosen = input("Masukkan Nama Dosen: ")
                    try:
                        print(kampus.tambah_dosen(id_dosen, nama_dosen))
                        print("Dosen berhasil ditambahkan!")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif sub_pilihan == "2":
                    if len(kampus.dosen_list) == 0:
                        print("Error: Belum ada data Dosen yang tersedia")
                        continue
                    id_dosen = input("Masukkan ID Dosen: ")
                    try:
                        print(kampus.detail_dosen(id_dosen))
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Pilihan tidak valid!")
                    
        elif pilihan == "2":
            while True:
                print("\n=== MANAJEMEN MATAKULIAH ===")
                print("1. Tambah Matakuliah")
                print("2. Lihat Detail Matakuliah")
                print("0. Kembali ke Menu Utama")
                
                sub_pilihan = input("\nMasukkan pilihan (0-2): ")
                
                if sub_pilihan == "0":
                    break
                elif sub_pilihan == "1":
                    kode_mk = input("Masukkan Kode Matakuliah: ")
                    nama_mk = input("Masukkan Nama Matakuliah: ")
                    try:
                        print(kampus.tambah_matakuliah(kode_mk, nama_mk))
                        print("Matakuliah berhasil ditambahkan!")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif sub_pilihan == "2":
                    if len(kampus.matakuliah_list) == 0:
                        print("Error: Belum ada data Matakuliah yang tersedia")
                        continue
                    kode_mk = input("Masukkan Kode Matakuliah: ")
                    try:
                        print(kampus.detail_matakuliah(kode_mk))
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Pilihan tidak valid!")
                    
        elif pilihan == "3":
            while True:
                print("\n=== MANAJEMEN MAHASISWA ===")
                print("1. Tambah Mahasiswa")
                print("2. Lihat Detail Mahasiswa")
                print("0. Kembali ke Menu Utama")
                
                sub_pilihan = input("\nMasukkan pilihan (0-2): ")
                
                if sub_pilihan == "0":
                    break
                elif sub_pilihan == "1":
                    nim = input("Masukkan NIM Mahasiswa: ")
                    nama = input("Masukkan Nama Mahasiswa: ")
                    try:
                        print(kampus.tambah_mahasiswa(nim, nama))
                        print("Mahasiswa berhasil ditambahkan!")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif sub_pilihan == "2":
                    if len(kampus.mahasiswa_list) == 0:
                        print("Error: Belum ada data Mahasiswa yang tersedia")
                        continue
                    nim = input("Masukkan NIM Mahasiswa: ")
                    try:
                        print(kampus.detail_mahasiswa(nim))
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Pilihan tidak valid!")
                    
        elif pilihan == "4":
            if len(kampus.dosen_list) == 0:
                print("Error: Belum ada data Dosen. Silakan tambahkan Dosen terlebih dahulu")
                continue
            if len(kampus.matakuliah_list) == 0:
                print("Error: Belum ada data Matakuliah. Silakan tambahkan Matakuliah terlebih dahulu")
                continue
            if len(kampus.mahasiswa_list) == 0:
                print("Error: Belum ada data Mahasiswa. Silakan tambahkan Mahasiswa terlebih dahulu")
                continue

            while True:
                print("\n=== MANAJEMEN PERKULIAHAN ===")
                print("1. Tambah Perkuliahan")
                print("2. Lihat Detail Perkuliahan")
                print("0. Kembali ke Menu Utama")
                
                sub_pilihan = input("\nMasukkan pilihan (0-2): ")
                
                if sub_pilihan == "0":
                    break
                elif sub_pilihan == "1":
                    id_perkuliahan = input("Masukkan ID Perkuliahan: ")
                    id_dosen = input("Masukkan ID Dosen: ")
                    kode_mk = input("Masukkan Kode Matakuliah: ")
                    waktu = input("Masukkan Waktu (contoh: Senin 09:00): ")
                    try:
                        print(kampus.tambah_perkuliahan(id_perkuliahan, id_dosen, kode_mk, waktu))
                        print("Perkuliahan berhasil ditambahkan!")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif sub_pilihan == "2":
                    if len(kampus.perkuliahan_list) == 0:
                        print("Error: Belum ada data Perkuliahan yang tersedia")
                        continue
                    id_perkuliahan = input("Masukkan ID Perkuliahan: ")
                    try:
                        print(kampus.detail_perkuliahan(id_perkuliahan))
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Pilihan tidak valid!")
        
        else:
            print("Pilihan tidak valid!")
