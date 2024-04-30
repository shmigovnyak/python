dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
mnog1 = set()
mnog2 = set()
for key, value in dct.items():
    mnog1.add(key)
    mnog2.add(value)
mnog3 = mnog1.union(mnog2)
print(mnog3)

