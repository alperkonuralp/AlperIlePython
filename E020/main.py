

def topla(a, b):
    toplam = a + b
    if a < b:
        kucuk = a
    else:
        kucuk = b
    return (toplam, kucuk)


toplam, kucuk = topla(1, 2)

print(toplam, kucuk)


tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
tuple3 = tuple([1, 2, 3, 4, 5])


ilkSayi = tuple2[0]
ikinciSayi = tuple2[1]
ucuncuSayi = tuple2[2]

ilkSayi, ikinciSayi, ucuncuSayi = tuple2




a = [1, 2, 3, 4, 5]

print(a)

print(a[1])

a.append(6)

print(a)

del a[2]

print(a)

b = (1, 2, 3)

print(b)

print(b[0])

# b.append(6) # Demetler (Tuple) değiştirilemezdir.
a[0] = 123
# b[0] = 123






