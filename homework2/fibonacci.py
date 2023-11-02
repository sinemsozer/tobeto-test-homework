# İlk iki Fibonacci sayısı belirleniyor
a , b = 1, 1

# En az 20 elemanlı Fibonacci serisi oluşturuluyor
fibonacci_seri = [a, b]

while len(fibonacci_seri) < 20:
    # Son iki sayı toplanıp yeni sayı hesaplanıyor
    yeni_sayi = a + b

    # Yeni sayı listeye ekleniyor
    fibonacci_seri.append(yeni_sayi)

    # Yeni sayılar güncelleniyor
    a, b = b, yeni_sayi

# Oluşturulan Fibonacci serisini yazdır
print(fibonacci_seri)