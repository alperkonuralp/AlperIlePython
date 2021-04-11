
def topla(*sayilar):
    print(sayilar)
    toplam = 0
    for i in sayilar:
        toplam += i
    return toplam

print(topla(2, 3, 4, 5, 6))


def carp(a, b, *sayilar):
    print(sayilar)
    carpim = a * b
    for i in sayilar:
        carpim *= i
    return carpim


print(carp(2, 3, 4))

