def call_info_decorator(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами {args_str} и именованными аргументами {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@call_info_decorator
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