from datetime import datetime


def log_yaz(level, message):
    # print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {level} {message}')
    # print()
    print(f'{{"datetime":"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}","level":"{level}","message":"{message}"}}')


# print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO Uygulama başladı.')
log_yaz('INFO', 'Uygulama başladı.')


# ....

# print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} DEBUG İlk işlem tamam.')
log_yaz('DEBUG', 'İlk işlem tamam.')


# ....

# print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} DEBUG İkinci işlem tamam.')
log_yaz('DEBUG', 'İkinci işlem tamam.')

# ....

a = 25

# print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} DEBUG Üçüncü işlem tamam. a = {a}')
log_yaz('DEBUG', f'Üçüncü işlem tamam. a = {a}')


# ....

# print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO Uygulama Bitti.')
log_yaz('INFO', 'Uygulama Bitti.')

