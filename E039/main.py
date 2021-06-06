# from os import path
#
# fn = input('Dosya Adını Giriniz : ')
#
# if path.exists(fn):
#     with open(fn, 'rt') as f:
#         c = f.read()
#         print(c)
#
# else:
#     print("Dosya bulunamadı.")
from io import TextIOWrapper

fn = input('Dosya Adını Giriniz : ')
f = False
try:
    # print(5/0)
    f = open(fn, 'rt')
    print(type(f))
    c = f.read()
    print(c)
# except ZeroDivisionError:
#     print('Sıfıra bölme hatası')

except FileNotFoundError as fnfe:
    print('Dosya bulunamadı. ', fnfe.filename)

except:
    print('İşlem sırasında bir hata oluştu. Lütfen sonra tekrar deneyiniz.')

else:
    print(fn, 'isimli dosya okundu.')

finally:
    if f is TextIOWrapper and not f.closed:
        f.close()
