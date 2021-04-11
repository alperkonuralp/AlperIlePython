from time import time


def veriEkle(data, **parameters):
    print(parameters)
    print(type(parameters))

    for i in data:
        for k in parameters.keys():
            i[k] = parameters[k]



veriler = [
    {"id": 1, "ad": "Alper", "soyad": "Konuralp"},
    {"id": 2, "ad": "Burcu", "soyad": "Konuralp"},
    {"id": 3, "ad": "Yağmur", "soyad": "Konuralp"},
]

print(veriler)

# veriEkle(data=veriler, parameterName="yas")
# veriEkle(parameterName="dogumGunu", data=veriler)

veriEkle(veriler, yas=0, dogumGunu=time(), sehir="İstanbul")

print(veriler)
