import os
from datetime import datetime


def getFileAndDirectoryList(directoryPath):
    elements = [{
        "fullName": x[1],
        "name": x[0],
        "type": "D" if os.path.isdir(x[1]) else "F",
        "size": os.path.getsize(x[1]) if os.path.isfile(x[1]) else None,
        "creationDate": datetime.fromtimestamp(os.path.getctime(x[1]))
    }
        for x in ([(y, os.path.join(directoryPath, y)) for y in os.listdir(directoryPath)])
    ]
    return elements


print(os.getcwd())

print(getFileAndDirectoryList(os.getcwd()))

dirName = os.path.join(os.getcwd(), "data2")
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("dizin oluşturuldu.")
else:
    print("Dizin zaten var.")
