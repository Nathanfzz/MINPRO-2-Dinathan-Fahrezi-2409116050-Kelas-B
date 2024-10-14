Flowchart:![MINPRO 2 ](https://github.com/user-attachments/assets/d8e99db4-6e95-45ee-b182-2e3c8ab83321)

# MINPRO-2-Dinathan-Fahrezi-2409116050-Kelas-B
Import dan Data Awal:
![Screenshot 2024-10-14 235426](https://github.com/user-attachments/assets/4633db51-2a04-4e66-a98f-2698189f925e)
Mengimpor PrettyTable dari modul prettytable. Ini digunakan untuk membuat tabel yang rapi saat menampilkan data.
Ada list bernama 'pemain' yang berisi dictionary. Setiap dictionary mewakili seorang pemain dengan informasi nama, posisi, status, dan kesehatan.
Fungsi Register dan Login:

Fungsi register():
Meminta input nama dan password baru dari pengguna.
Mengembalikan dictionary dengan kunci 'nama' dan 'pass'.
![Screenshot 2024-10-15 000443](https://github.com/user-attachments/assets/33d30c62-90c5-42ef-bb2a-ae2e5246d331)
Fungsi login():
Mirip dengan register, tapi untuk proses login.
Juga mengembalikan dictionary dengan format yang sama.

Proses Registrasi dan Login:
Memulai dengan meminta pengguna untuk register.
Kemudian, ada loop while yang akan terus berjalan sampai login berhasil.
Jika data login tidak cocok dengan data registrasi, pengguna diminta untuk mencoba lagi.

Fungsi menuadmin():
![Screenshot 2024-10-15 000628](https://github.com/user-attachments/assets/9c2a1f31-4f11-4b98-b1f6-36b9f413976c)
![Screenshot 2024-10-14 233225](https://github.com/user-attachments/assets/bc0d74c9-f744-4faf-aab2-b7a5b65845b8)
Menampilkan menu admin dengan 5 pilihan.
Opsi 1: Tambah Data Pemain
Meminta input detail pemain baru dan menambahkannya ke list 'pemain'.
![Screenshot 2024-10-14 233312](https://github.com/user-attachments/assets/50ee5555-6a59-471f-827b-41df53eed837)

Opsi 2: Lihat Data Pemain
Menggunakan PrettyTable untuk menampilkan data semua pemain dalam bentuk tabel.
![Screenshot 2024-10-14 233333](https://github.com/user-attachments/assets/25ee639d-60c2-4149-8be0-a26e49e4f71b)

Opsi 3: Update Data Pemain
Mencari pemain berdasarkan nama dan memperbarui informasinya.
![Screenshot 2024-10-14 234049](https://github.com/user-attachments/assets/4e37fafa-b3a6-4ec9-9117-f22a642a1f17)
![Screenshot 2024-10-14 234059](https://github.com/user-attachments/assets/83375f86-7770-4af3-a35c-a33fc652ee54)

Opsi 4: Hapus Data Pemain
Menghapus data pemain dari list berdasarkan nama.
![Screenshot 2024-10-14 234159](https://github.com/user-attachments/assets/6b7ca239-3276-4638-a608-4313cd3b4d02)

Opsi 5: Keluar.

Menu Utama:
![image](https://github.com/user-attachments/assets/4eeae816-f938-4bc4-be88-54fe414fd1e3)
Menampilkan pilihan untuk masuk sebagai admin atau pemain.
Jika memilih admin, pengguna diminta memasukkan kode verifikasi.
Jika kode benar, program menjalankan fungsi menuadmin().
Jika memilih pemain, program langsung menjalankan fungsi menuuser().

Penanganan Error:

saya menggunakan banyak kondisional (if-else) untuk menangani berbagai kemungkinan input.
Jika input tidak valid, program akan memberi tahu pengguna dan meminta input ulang.

Struktur Loop:
saya menggunakan beberapa loop while untuk membuat menu yang terus berjalan sampai pengguna memilih untuk keluar.

Manipulasi Data:
saya menggunakan operasi list dan dictionary untuk menambah, mengubah, dan menghapus data pemain.

Input/Output:
Program banyak menggunakan fungsi input() untuk menerima input dari pengguna.
Fungsi print() digunakan untuk menampilkan informasi dan menu kepada pengguna.
