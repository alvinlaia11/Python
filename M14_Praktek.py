import os

def clr():
    os.system('cls')

class Jenis:
    def __init__(self, jenis):
        self.jenis = jenis
    
    def tambah(self):
        print(f"\nJenis kendaraan {self.jenis} berhasil ditambahkan")
    
    def detail(self):
        print(f"Jenis kendaraan: {self.jenis}")

class Tipe:
    def __init__(self, tipe):
        self.tipe = tipe
    
    def tambah(self, jumlah):
        print(f"\nKendaraan tipe {self.tipe} sebanyak {jumlah} unit berhasil ditambahkan")
    
    def detail(self):
        print(f"Tipe kendaraan: {self.tipe}")

class Garasi:
    def __init__(self):
        self.jenis_list = []
        self.tipe_list = []
    
    def tambahStok(self):
        if not self.jenis_list:
            print("\nBelum ada jenis kendaraan yang tersedia!")
            print("Silahkan tambah jenis kendaraan terlebih dahulu.")
            return
        
        print("\nPilih Jenis Kendaraan:")
        for i, jenis in enumerate(self.jenis_list, 1):
            print(f"{i}. {jenis.jenis}")
        
        try:
            pilihan = int(input("Jenis : "))
            if 1 <= pilihan <= len(self.jenis_list):
                jenis_dipilih = self.jenis_list[pilihan-1]
                
                tipe_tersedia = []
                for j, t, _ in self.tipe_list:
                    if j == jenis_dipilih and t.tipe not in [x.tipe for x in tipe_tersedia]:
                        tipe_tersedia.append(t)
                
                if not tipe_tersedia:
                    print(f"\nBelum ada tipe kendaraan untuk {jenis_dipilih.jenis}")
                    print("Silahkan tambah kendaraan terlebih dahulu di menu 2")
                    return
                
                print(f"\nPilih Tipe {jenis_dipilih.jenis}:")
                for i, tipe in enumerate(tipe_tersedia, 1):
                    print(f"{i}. {tipe.tipe}")
                
                try:
                    pilihan_tipe = int(input("Pilihan Tipe : "))
                    if 1 <= pilihan_tipe <= len(tipe_tersedia):
                        tipe_dipilih = tipe_tersedia[pilihan_tipe-1]
                        try:
                            jumlah = int(input("Masukkan jumlah : "))
                            self.tipe_list.append((jenis_dipilih, tipe_dipilih, jumlah))
                            tipe_dipilih.tambah(jumlah)
                        except ValueError:
                            print("\nJumlah harus berupa angka!")
                    else:
                        print("\nPilihan tidak valid!")
                except ValueError:
                    print("\nMasukkan angka yang valid!")
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nMasukkan angka yang valid!")
    
    def tambahKendaraan(self):
        if not self.jenis_list:
            print("\nBelum ada jenis kendaraan yang tersedia!")
            return
            
        print("\nMenu Tambah Kendaraan Baru")
        print("\nPilihan Jenis:")
        for i, jenis in enumerate(self.jenis_list, 1):
            print(f"{i}. {jenis.jenis}")
        
        try:
            pilihan = int(input("Pilihan Jenis : "))
            if 1 <= pilihan <= len(self.jenis_list):
                tipe = input("Tipe Baru : ")
                new_tipe = Tipe(tipe)
                self.tipe_list.append((self.jenis_list[pilihan-1], new_tipe, 1))
                new_tipe.tambah(1)
            else:
                print("\nPilihan tidak valid!")
        except ValueError:
            print("\nMasukkan angka yang valid!")
    
    def tambahJenis(self):
        tipe = input("Tipe Baru : ")
        new_jenis = Jenis(tipe)
        self.jenis_list.append(new_jenis)
        new_jenis.tambah()
    
    def detailKendaraan(self):
        if not self.jenis_list:
            print("Tidak ada kendaraan dalam garasi")
            return
            
        print("\nDaftar Kendaraan:")
        for jenis in self.jenis_list:
            print(f"\n{jenis.jenis}:")
            
            tipe_dict = {}
            for j, t, jml in self.tipe_list:
                if j == jenis:
                    if t.tipe in tipe_dict:
                        tipe_dict[t.tipe] += jml
                    else:
                        tipe_dict[t.tipe] = jml
            
            if tipe_dict:
                for tipe, jumlah in tipe_dict.items():
                    print(f"    {tipe:<15} {jumlah} unit")
            else:
                print("    Belum ada kendaraan")

clr()
obj = Garasi()
while True:
    print("\nMenu:")
    print("1. Tambah Jenis Baru")
    print("2. Tambah Kendaraan")
    print("3. Tambah Stok")
    print("4. Detail Kendaraan")
    print("0. Keluar")
    
    pilihan = input("Pilihan : ")
    
    if pilihan == "1":
        clr()
        obj.tambahJenis()
    elif pilihan == "2":
        clr()
        obj.tambahKendaraan()
    elif pilihan == "3":
        clr()
        obj.tambahStok()
    elif pilihan == "4":
        clr()
        obj.detailKendaraan()
    elif pilihan == "0":
        clr()
        print("\nTerima kasih telah menggunakan program ini!")
        break
    else:
        print("\nPilihan tidak valid!")
    
    input("\nTekan Enter untuk melanjutkan...")
    clr()