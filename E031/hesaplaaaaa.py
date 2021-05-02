
def ortalamaHesapla(hesaplanacakListe):
    toplam = 0
    for eleman in hesaplanacakListe:
        toplam += eleman

    return toplam / len(hesaplanacakListe)


def standartSapmaHesapla(hesaplanacakListe):
    ortalama = ortalamaHesapla(hesaplanacakListe)
    toplam = 0
    for eleman in hesaplanacakListe:
        toplam += (eleman - ortalama) ** 2

    return (toplam / (len(hesaplanacakListe) - 1)) ** 0.5
