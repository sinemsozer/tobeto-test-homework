n = int(input("Bir sayı giriniz:"))

sum = 0
for i in range (1,n):
    if n % i ==0:
        sum += i
if sum == n:
    print(n, "bir mükemmel sayıdır.")
else:
    print(n, "bir mükemmel sayı değildir.")