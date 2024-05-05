def fibonacci_generator(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

n = int(input("Введите количество чисел Фибоначчи: "))

for num in fibonacci_generator(n):
    print(num)