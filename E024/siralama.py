# liste = [35, 17, 1, 45, 23, 36, 11, 0]
# liste = [0, 1, 11, 17, 23, 35, 36, 45]

def sirala(liste):
    for i in range(0, len(liste) - 1):
        degistirildi = False
        for j in range(0, len(liste) - 1 - i):
            if liste[j] > liste[j+1]:
                a = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = a
                degistirildi = True

        if not degistirildi:
            break


# liste = [35, 17, 1, 45, 23, 36, 11, 0]
# liste = [0, 1, 11, 17, 23, 35, 36, 45]
liste = [11, 17, 0, 1, 36, 45, 23, 35]
sirala(liste)

print(liste)
