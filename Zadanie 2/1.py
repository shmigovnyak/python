kolvo = int(input('Введите кол-во элементов: '))
elements = []
count = 0
new_elements = []
while count < kolvo:
    element = input("Введите число или строку: ")
    elements.append(element)
    count = count + 1
stepen = int(input("Введите степень:"))
for i in elements:
    try:
        number = int(i)
        new_elements.append(number ** stepen)
    except ValueError:
        new_elements.append(i * stepen)

print(new_elements)
