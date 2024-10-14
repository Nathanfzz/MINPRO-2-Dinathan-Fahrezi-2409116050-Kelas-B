from prettytable import PrettyTable

pemain = [
    {"pemain": "Stephen Curry", "posisi": "PG", "status": "Inti", "kesehatan": "Sehat"},
    {"pemain": "Kevin Durant", "posisi": "SF", "status": "Inti", "kesehatan": "Sehat"},
    {"pemain": "Draymond Green", "posisi": "PF", "status": "Inti", "kesehatan": "Sehat"},
    {"pemain": "Andre Iguodala", "posisi": "SF", "status": "Inti", "kesehatan": "Sehat"},
    {"pemain": "Damian Jones", "posisi": "C", "status": "Cadangan", "kesehatan": "Sehat"},
    {"pemain": "Shaun Livingston", "posisi": "PG", "status": "Cadangan", "kesehatan": "Sehat"},
    {"pemain": "Klay Thompson", "posisi": "SG", "status": "Inti", "kesehatan": "Sehat"}
]

def register():
    namabaru = input("Masukkan nama baru anda: ")
    passbaru = input("Masukkan password baru anda: ")
    return {"nama": namabaru, "pass": passbaru}

def login():
    print("Silahkan melanjutkan dengan login")
    namalogin = input("Masukkan nama anda: ")
    passlogin = input("Masukkan password anda: ")
    return {"nama": namalogin, "pass": passlogin}
print("Silahkan register terlebih dahulu")
while True:
    if register () == login(): 
        break
    else:
        print("Nama atau password anda salah")
        pass



def menuadmin():
    while True:
        print(" ================================")
        print("|          Menu Admin            |")
        print("|     1. Tambah Data Pemain      |")
        print("|     2. Lihat Data Pemain       |")
        print("|     3. Update Data Pemain      |")
        print("|     4. Hapus Data Pemain       |")
        print("|     5. Kembali                 |")
        print(" ================================")
        option = int(input("Selamat datang pelatih, ada perlu apa hari ini?: "))
        if option == 1:
            nama = input("Masukkan nama pemain: ")
            posisi = input("Masukkan posisi pemain: ")
            status = input("Masukkan status pemain: ")
            kesehatan = input("Masukkan status kesehatan pemain: ")
            pemain.append({"pemain": nama, "posisi": posisi, "status": status, "kesehatan": kesehatan})
            print("Data pemain berhasil ditambahkan.")
        elif option == 2:
            table = PrettyTable()
            table.field_names = ["Pemain", "Posisi", "Status", "Kesehatan"]
            for p in pemain:
                table.add_row([p["pemain"], p["posisi"], p["status"], p["kesehatan"]])
            print(table)
        elif option == 3:
            nama = input("Masukkan nama pemain yang ingin diupdate: ")
            for p in pemain:
                if p["pemain"].lower() == nama.lower():
                    p["posisi"] = input("Masukkan posisi baru: ")
                    p["status"] = input("Masukkan status baru: ")
                    p["kesehatan"] = input("Masukkan status kesehatan baru: ")
                    print("Data pemain berhasil diupdate.")
                    break
            else:
                print("Pemain tidak ditemukan.")
        elif option == 4:
            nama = input("Masukkan nama pemain yang ingin dihapus: ")
            for p in pemain:
                if p["pemain"].lower() == nama.lower():
                    pemain.remove(p)
                    print("Data pemain berhasil dihapus.")
                    break
            else:
                print("Pemain tidak ditemukan.")
        elif option == 5:
            break
        else:
            print("Pilihan anda tidak valid")
            pass

def menuuser():
    while True:
        print(" ================================")
        print("|          Menu Pemain           |")
        print("|     1. Lihat Status Pemain     |")
        print("|     2. Kembali                 |")
        print(" ================================")
        option = int(input("Silakan pilih opsi: "))
        if option == 1:
            nama = input("Masukkan nama anda: ")
            for p in pemain:
                if p["pemain"].lower() == nama.lower():
                    table = PrettyTable()
                    table.field_names = ["Pemain", "Posisi", "Status", "Kesehatan" ]
                    
                    table.add_row([p["pemain"], p["posisi"], p["status"], p["kesehatan"] ])
                    print(table)
                    break
            else:
                print("Pemain tidak ditemukan.")
        elif option == 2:
            nama = input("Masukkan nama anda: ")
            catatan = input("Masukkan catatan: ")
            for p in pemain:
                if p["pemain"].lower() == nama.lower():
                    p["catatan"].append(catatan)
                    print("Catatan berhasil ditambahkan.")
                    break
            else:
                print("Pemain tidak ditemukan.")
        elif option == 3:
            break
        else:
            print("Pilihan anda tidak valid")
            pass

kodeverifpelatih = "tes"
print("Menu utama \n 1. Masuk sebagai pelatih/admin \n 2. Masuk sebagai Pemain/user")
option = int(input("Masukkan pilihan anda: "))
if option == 1:
    while True:
        if input("Masukkan kode verifikasi: ") == kodeverifpelatih:
            menuadmin()
            break
        else:
            print("Kode yang anda masukkan salah")
elif option == 2:
    menuuser()
else:
    print("Pilihan tidak valid.")
    pass