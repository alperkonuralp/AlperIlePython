
with open('logo-social-sq.jpg', 'rb') as f:
    content = f.read()

print(content)


with open('logo-social-sq.jpg', 'rb') as f:
    content2 = f.read(100)

print(content2)


with open('logo2.jpg', 'wb') as f:
    f.write(content)

