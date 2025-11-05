
budget = int(input("Berapa budget kamu? " ))

if budget == 1000000:
    print ("Kamu hanya dapat memesan tiket dengan kelas penerbangan Ekonomi ")
    print("=== Tiket Berhasil Dipesan ===")
    print ("Kelas        : Ekonomi")
    print ("Maskapai     : Lion Air")

    print ("---Terima Kasih Telah Memesan ---")
    print( "kelompok 17")
    exit()


elif budget > 1000000:
    print ("Kelas Penerbangan yang tersedia : ")
    print ("1. Ekonomi ")
    print ("2. Bisnis ")
    print ("3. First Class ")
    kelas = int(input("Pilih kelas penerbangan : "))

if kelas == 1:
        print ("Maskapai yang tersedia : ")
        print ("1. Lion Air ")
        print ("2. Citilink ")
        maskapal = int(input("Pilih Maskapai yang tersedia :  "))
        if maskapal == 1:
            namakelas = "Lion Air"
        elif maskapal == 2:
            namakelas = "Citilink"
        else : 
            print ("input salah")
            print( "kelompok 17")
            exit()
elif kelas == 2:
        print ("Maskapai yang tersedia : ")
        print ("1. Garuda ")
        print ("2. Batik Air ")
        maskapal = int(input("Pilih Maskapai yang tersedia : "))
        if maskapal == 1:
            namakelas = "Garuda"
        elif maskapal == 2:
            namakelas = "Batik Air"
        else : 
            print ("input salah")
            print( "kelompok 17")
            exit()
            
elif kelas == 3:
    print ("Maskapai yang tersedia : ")
    print ("1. Singapore Airlines ")    
    print ("2. Emirates ")
    maskapal = int(input("Pilih Maskapai yang tersedia : "))
    if maskapal == 1:
        namakelas = "Singapore Airlines"
    elif maskapal == 2:
        namakelas = "Emirates"

    else : 
        print ("input salah")
        print( "kelompok 17")
        exit()
else:
    print ("Uang tidak mencukupi ")
    print ("Kelompok 17")
    exit()
 



print("\n=== Tiket Berhasil Dipesan ===")
print(f"Kelas        : {'Ekonomi' if kelas==1 else 'Bisnis' if kelas==2 else 'First Class'}")
print(f"Maskapai     : {namakelas}")

if budget >= 10000000 and kelas == 2: 
    print ("Selamat kamu mendapatkan bonus Lounge Access")   
elif  budget >= 20000000 and kelas == 3:
     print ("Selamat kamu mendapatkan bonus Lounge access dan Hotel Gratis")
elif budget >= 10000000 and kelas ==3: 
    print ("Selamat kamu mendapatkan bonus Lounge Access") 
print( "kelompok 17")


