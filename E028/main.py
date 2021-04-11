
def topla(a, b): return a + b
print(topla(2, 3))


topla2 = lambda a, b: a + b
print(topla2(2, 3))


def listeyiGoster(liste, gosteriFonksiyonu):
    for i in liste:
        print(gosteriFonksiyonu(i))

list = [
    {"id": 1, "ad": "Alper", "soyad": "Konuralp" },
    {"id": 2, "ad": "Burcu", "soyad": "Konuralp"},
    {"id": 3, "ad": "Yağmur", "soyad": "Konuralp"},
]

listeyiGoster(list, lambda satir: f"{satir['ad']} {satir['soyad']}")
