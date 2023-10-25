sayi=(input("Lütfen bir sayı giriniz:"))

ters=sayi[::-1]

print("Girilen sayinin tersi = %s" % (ters))
if ters == sayi:
    print("Girilen sayı palindrom")
else:
    print("Girilen sayı palindrom değil")