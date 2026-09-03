def pola_sakit_kepala(panjang, lebar):
    panjang = abs(panjang)
    lebar = abs(lebar)

    if panjang != lebar:
        print("Panjang dan lebar harus sama!!")
    
    elif panjang % 2 == 0 or lebar % 2 == 0:
        print("Panjang dan lebar harus bilangan ganjil!!")

    else:
        tengah = panjang // 2

        for i in range(panjang):
            for j in range(lebar):
                nilai = 1 + abs(i - tengah) + abs(j - tengah)
                                
                digit = nilai % 10
                
                if j == lebar - 1:
                    print(digit)
                else:
                    print(digit, end=" ")
                
pola_sakit_kepala(7, 7)