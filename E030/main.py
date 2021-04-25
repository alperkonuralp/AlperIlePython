# 1 select * from tablo
# 2 select * from tablo where adi like 'A%'
# 3 select id, adi, soyadi from tablo where adi like 'A%'
# 4 select id, adi, soyadi from tablo where adi like 'A%' order by adi
# 5 select min(id) from tablo
# 6 select top 2 * from tablo , select * from tablo limit 2

# Linq in C#
# var l1 = from t in tablo;
# var l2 = from t in tablo where t.adi.StartWith("A");
# var l3 = from t in tablo where t.adi.StartWith("A") select new { t.id, t.adi, t.soyadi };
# var l5 = min(from t in tablo select t.id);



tablo = [
    {"id": 1, "adi": "Alper", "soyadi": "Konuralp"},
    {"id": 2, "adi": "Burcu", "soyadi": "Konuralp"},
    {"id": 3, "adi": "Yağmur", "soyadi": "Konuralp"},
]

# Linq in Python
# 1 select * from tablo
l1 = [x for x in tablo]

# 2 select * from tablo where adi like 'A%'
l2 = [x for x in tablo if x["adi"].startswith('A')]

# 3 select id, adi, soyadi from tablo where adi like 'A%'
l3 = [{"id": x["id"], "adi": x["adi"], "soyadi": x["soyadi"]} for x in tablo if x["adi"].startswith('A')]

# 5 select min(id) from tablo
l5 = min(x["id"] for x in tablo)
print(l5)

# 6 select top 2 * from tablo , select * from tablo limit 2
from itertools import islice

l6 = list(islice(tablo, 2))
print(l6)
