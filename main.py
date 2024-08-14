def lihat_saldo(saldo): # fungsi saldo (liat di line 35 )
    print("************************************************")
    print(f"Saldo anda Rp{saldo:.3f}") #tampilan jumlah saldo
def deposit():
    print("************************************************")
    jumlah = float(input("Masukan Jumlah uang yang ingin anda masukan: "))
    print("************************************************")
    if jumlah < 0:
        print("************************************************")
        print("Maaf, tolong Masukan jumlah uang yang benar")
        print("************************************************")
        return 0
    else:
        return jumlah

def ambil_uang(saldo):
    print("************************************************")
    jumlah = float(input("masukan jumlah uang yang ingin anda ambil:"))
    print("************************************************")

    if jumlah > saldo:
        print("************************************************")
        print("Maaf anda tidak memiliki uang sebanyak itu")
        print("************************************************")
        return 0
    elif jumlah < 0:
        print("************************************************")
        print("Jumlah harus lebih dari 0")
        print("************************************************")
        return 0
    else:
        return jumlah

def main():
    saldo = 0
    is_running = True

    while is_running :
        print("************************************************")
        print ("Selamat Datang Di ATM")
        print("************************************************")
        print ("1.Tunjukan Saldo")
        print("2.Memasukan Uang")
        print("3.Menarik Uang")
        print("4.Keluar")
        print("************************************************")
        pilih = input("Mohon dipilih dari nomor 1 hingga 4: ")

        if pilih == '1':
            lihat_saldo(saldo)
        elif pilih == '2':
            saldo += deposit()
        elif pilih == '3':
            saldo -= ambil_uang(saldo)
        elif pilih == '4':
            is_running = False
        else:
            print("************************************************")
            print("Tolong masukan nomor yang benar")
            print("************************************************")

    print("************************************************")
    print("Terima Kasih, Nikmati hari anda!")
    print("************************************************")

if __name__ == '__main__':
    main()