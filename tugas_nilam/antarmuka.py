from crud.read import read
from crud.create import create_record
from crud.update import update_record
from crud.delete import delete_record

def main():
    while True:
        print("\nMODIFIKASI DATABASE")
        print("-----------------------------------------")
        print("1. CREATE")
        print("2. READ")
        print("3. UPDATE")
        print("4. DELETE")
        print("5. EXIT")
        print("-----------------------------------------")

        pil = int(input("MASUKKAN PILIHAN: "))

        if pil == 1:
            nis = int(input("Masukkan  nis: "))
            nama = input("Masukkan nama: ")
            kelas = input("Masukan kelas: ")
            create_record( nis, nama, kelas )
            print("\nData berhasil ditambahkan\n.")
            read()

        elif pil == 2:
            read()

        elif pil == 3:
            nis = int(input("Masukkan nis : "))
            nama = input("Masukkan nama : ")
            kelas = input("Masukan kelas: ")
            update_record(nis, nama, kelas)
            print("\nData berhasil diupdate\n.")
            read()

        elif pil == 4:
            nis = int(input("Masukkan nis siswa yang ingin dihapus: "))
            delete_record(nis)
            print("\nData berhasil dihapus\n.")
            read()

        elif pil == 5:  
            print("Sampai Jumpa!")
            break
        else:
            print("Pilihan tidak ada. Silakan coba lagi.")

if __name__ == "__main__":
    main()