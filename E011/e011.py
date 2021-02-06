print("Hesap Makinası")
print("--------------\n")

print("İlk sayıyı giriniz:")
a = int(input())

print("İkinci sayıyı giriniz:")
b = int(input())

print("İşlem Seçiniz:")
print("1. Toplama")
print("2. Çıkarma")
print("3. Çarpma")
print("4. Bölme")
print("Diğer tuşlar çıkış")
c = input()

if c == "1":
    print('a + b =', a , '+', b, '=', a + b )
elif c == "2":
    print('a - b =', a , '-', b, '=', a - b )
elif c == "3":
    print('a * b =', a , '*', b, '=', a * b )
elif c == "4":
    print('a / b =', a , '/', b, '=', a / b )

print('İyi Günler')
