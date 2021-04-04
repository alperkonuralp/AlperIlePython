# 1 1 2 3 5 8 13 21 34 55 89 ....

def fibanocci(n):
    dizi = [1, 1]

    for i in range(2, n+1):
        dizi.append(dizi[i-2] + dizi[i-1])

    return dizi

print(fibanocci(20))

