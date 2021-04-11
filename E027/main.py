import time
import datetime

# time sınıfı ile epoch zamanını almak
# Time intervals are floating-point numbers in units of seconds.
# Particular instants in time are expressed in seconds since 00:00:00
# hrs January 1, 1970(epoch).
print('time.time() = ', time.time())
print('time.time_ns() = ', time.time_ns())

# anın zamanını almak ve göstermek
now = datetime.datetime.now()
print('now =', now)
print('type(now) =', type(now))
print("now.strftime('%d.%m.%Y %H:%M:%S') = ", now.strftime('%d.%m.%Y %H:%M:%S'))

# bugün böyle söylenmiyor.
today1 = datetime.datetime.today()
print('today1 =', today1)
print('type(today1) =', type(today1))
print("today1.strftime('%d.%m.%Y %H:%M:%S') = ", today1.strftime('%d.%m.%Y %H:%M:%S'))

# bugün
today = datetime.date.today()
print("today = ", today)
print('type(today) =', type(today))
print("today.strftime('%d.%m.%Y') = ", today.strftime('%d.%m.%Y'))

# dün
yesterday = today - datetime.timedelta(days=-1)
print("yesterday = ", yesterday)

bugün = datetime.datetime(today.year, today.month, today.day)
print("bugün = ", bugün)

dün = bugün - datetime.timedelta(days=1)
print("dün = ", dün)


tarih1 = datetime.datetime.now()
tarih2 = datetime.datetime(2021, 4, 5)

farksüre = tarih1 - tarih2
print("farksüre = ", farksüre)
print("type(farksüre) = ", type(farksüre))






# epoch dan datetime'a çevirim
now2 = datetime.datetime.fromtimestamp(time.time())
print("now2 = ", now2)
print("type(now2) = ", type(now2))

# datetime'dan epoch a çevirim.
timestamp = now.timestamp()
print("timestamp =", timestamp)



