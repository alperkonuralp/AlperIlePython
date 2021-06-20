
print("Merhaba")

a = float(input("ilk sayı:"))

b = float(input("ikinci sayı:"))
# if b == 0.0:
#     print("Lütfen 0'dan farklı bir sayı giriniz.")
# else:
#     print(" a / b = ", a, "/", "b = ", a / b)

try:
    print(" a / b = ", a, "/", "b = ", a / b)
except ZeroDivisionError as zde:
    print("Lütfen 0'dan farklı bir sayı giriniz.")
except MemoryError as me:
    print("Hafıza Hatası :", me)
else:
    print("İşlem hatasız.")
finally:
    print("İşlem Bitti!...")
