
with open('Yazi.txt', 'r') as f:
    content = f.read() # Dosyanın tamamını okuduk
    # print(content)

with open('Yazi.txt', 'r') as f:
    content = f.read(100) # Dosyanın ilk 100 karakterini okuduk
    print(content)

with open('Yazi.txt', 'r') as f:
    content = f.readline() # Dosyanın ilk satırını okuduk
    print(content)


with open('Yazi.txt', 'r') as f:
    rows = []
    content = f.readline() # Dosyanın ilk satırını okuduk
    rows.append(content)
    while content:
        content = f.readline()  # Dosyanın diğer satırlarını okuduk
        rows.append(content)

    print(rows)


with open('Yazi.txt', 'r') as f:
    rows = f.readlines() # Dosyanın bütün satırını okuduk

    print(rows)



with open('Yazi.txt', 'r') as f:
    rows = []
    for i in f:
        rows.append(i)

    print(rows)
