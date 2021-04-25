liste = [0, 1, 2, 3, 4, 5]

liste = list(range(0, 6))

# ikininKatlari = [2**0, 2**1, 2**2, 2**3]
ikininKatlari = []

for i in liste:
    if i % 2 == 0:
        ikininKatlari.append(2**i)

ikininKatlari2 = [2**i for i in liste if i % 2 == 0]

print(ikininKatlari)
print(ikininKatlari2)




from data import data

print(len(data))

isimListesi = [ f'{x["name"]["first"]} {x["name"]["last"]}' for x in data ]

print(isimListesi)


# kisiler = [ x for x in data if x["isActive"] ]
kisiler = [ x for x in data if x["isActive"] and "Lorem" in x["tags"] ]

print(len(kisiler))
# print(kisiler)





