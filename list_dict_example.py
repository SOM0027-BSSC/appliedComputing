d = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

dkeys = ["brand", "model", "year"]

l = ["a", "b", "c", "d", "e", "f"]

for i in d.keys():
    print(f"{i}: {d[i]}")