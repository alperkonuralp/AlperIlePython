import os

filename = os.path.join(os.getcwd(), "data.json")

# f = open(filename)
with open(filename, mode="w") as f:
    print("name :", f.name)
    print("mode :", f.mode)
    print("buffer :", f.buffer)
    print("encoding :", f.encoding)
    print("closed :", f.closed)
    print("errors :", f.errors)

print("closed :", f.closed)
