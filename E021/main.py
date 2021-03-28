a = [1, 2, 3]
b = (1, 2, 3)
a1 = a[1:]

print(a1)

c = { 100: 1254, 101: 1593, 102: 2021 }

print(c)

print(a[0])
print(b[0])
print(c[100])

c[103] = 123
print(c)

c[1] = 123
print(c)

print(c[1])


d = { "İsim": "Alper", "Soyad": "Konuralp", "Yaş": 43 }

print(d)
print(d["İsim"], d["Soyad"])

if "abc" in d.keys():
    print(d["abc"])
else:
    print("Yok")

print(d.keys())
print(d.values())
