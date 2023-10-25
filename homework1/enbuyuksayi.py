num1 = int(input("Lütfen birinci sayıyı giriniz: "))
num2 = int(input("Lütfen ikinci sayıyı giriniz: "))
num3 = int(input("Lütfen ücüncü sayıyı giriniz: "))

if (num1 > num2) and (num1 > num3):
   print("En büyük sayı :" , num1) 
elif (num2 > num1) and (num2 > num3):
    print("En büyük sayı :" , num2)
else:
   print("En büyük sayı :" , num3)