sayi1= int(input("1. sayıyı giriniz: "))
sayi2= int(input("2. sayıyı giriniz: "))
def ebobEkokBul(sayi1,sayi2):
    if sayi1>=sayi2:
        kucukSayi=sayi2
    else:
        kucukSayi=sayi1
    for i in range(1,kucukSayi+1):
        if(sayi1%i==0 & sayi2%i==0):
            ebob=i
    print("EBOB: ", ebob)
    ekok=(sayi1*sayi2)//ebob
    print("EKOK: ", ekok)
ebobEkokBul(sayi1,sayi2)

# ikinci yöntem

def ebob(sayi1, sayi2):     
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2     
    return sayi1                                    

def ekok(sayi1, sayi2):                             
    return sayi1 * sayi2 // ebob(sayi1, sayi2)         

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))    

ebob_sonuc = ebob(sayi1, sayi2)
ekok_sonuc = ekok(sayi1, sayi2)

print(sayi1, "ve", sayi2, "sayılarının EBOB'u:",ebob_sonuc)
print(sayi1, "ve", sayi2, "sayılarının EKOK'u:",ekok_sonuc)