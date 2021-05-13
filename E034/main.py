from datetime import datetime

now = datetime.now()

with open('deneme.txt', 'w', encoding='utf8') as f:
    print(f.name)
    f.write('Merhaba Dünya\n')
    f.write(f'Bugün {now}.\n')
    f.write("""<p>
    Bu bir paragraf
</p>
""")

dizi = [
    '<html>\n',
    '<head>\n',
    '    <title>İlk Dosya</title>\n',
    '</head>\n',
    '<body>\n'
]

for i in range(10):
    dizi.append(f'    <p>{i+1}. Satır</p>\n')

dizi.append('</body>\n')
dizi.append('</html>\n')

with open('deneme.html', 'w', encoding='utf8') as f:
    f.writelines(dizi)

