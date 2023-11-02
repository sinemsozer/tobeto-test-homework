def asal_carpanlari_bul(sayi):   
    carpanlar = []
    bolen = 2
    
    while sayi > 1:
        while sayi % bolen == 0:      
            carpanlar.append(bolen)    
            sayi //= bolen    
        bolen += 1
    
    return carpanlar

sayi = int(input("Bir sayı giriniz: "))

if sayi < 2:
    print("2 veya daha büyük bir sayı giriniz.")
else:
    asal_carpanlar = asal_carpanlari_bul(sayi)
    print(f"{sayi}'nin asal çarpanları: , asal_carpanlar")