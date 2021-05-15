import os
from datetime import datetime

fileName = "a.txt"

if not os.path.exists(fileName):
    with open(fileName, 'w') as f:
        f.write("0\n")

with open(fileName, "r+") as f:
    number = int(f.readline())
    number += 1
    f.seek(0, 0)
    f.write(f"{number}\n")

    f.seek(0, 2)
    f.write(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    f.write("\n")

    print(f"File Size : {f.tell()}")
    print(f"File Size : {os.path.getsize(fileName)}")
