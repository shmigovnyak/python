chislo = int(input())
chisla = []

for i in range(-chislo, chislo + 1):
    chisla.append(i)
print(chisla)
plus_chisla = []
minus_chisla = []
for i in chisla:
    if i>0:
        plus_chisla.append(i)
    else:
        minus_chisla.append(i)
print('сумма положительных чисел:',sum(plus_chisla))
print('сумма отрицательных чисел:',sum(minus_chisla))
