

def topla(a, b):
    toplam = a + b
    return toplam


def hesapla(a, b, c, d, e, f):
    toplam = a + b + c + d + e + f
    ortalama = toplam / 6
    return [toplam, ortalama]

toplamDegeri = topla(3, 5)

print("Toplam Değeri =", toplamDegeri)

toplamDegeri2 = topla(topla(3, 5), topla(5, 7))
print("Toplam Değeri 2 =", toplamDegeri2)

toplamDegeri3 = hesapla(1, 2, 3, 4, 5, 6)
print(f"Toplam = {toplamDegeri3[0]}, Ortalama = {toplamDegeri3[1]}")



