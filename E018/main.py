from datetime import datetime


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_full_name(first_name, last_name):
    print(f'{first_name} {last_name}')


def log_yaz(message, level='INFO'):
    # print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {level} {message}')
    # print()
    print(f'{{"datetime":"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}","level":"{level}","message":"{message}"}}')


log_yaz('Uygulama Başladı', 'DEBUG')
print_hi('PyCharm')
print_full_name('alper', 'konuralp')
print_full_name(first_name='Alper', last_name='Konuralp')
print_full_name(last_name='Konuralp', first_name='Ali')

log_yaz('Uygulama Bitti')
