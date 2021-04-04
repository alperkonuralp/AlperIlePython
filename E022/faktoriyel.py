
# 1! = 1
# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 100! = 1 * 2 * ..... * 100

def faktoriyel(n):
    """ Bu fonksiyon parametrede girilen sayının faktöriyelini bulur.
    :param n faktöriyeli bulunacak sayı
    """
    carpim = 1
    for k in range(2, n+1):
        carpim *= k

    return carpim


print("5! =", faktoriyel(5))
