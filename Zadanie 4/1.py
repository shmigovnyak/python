#Список квадратов первых 10 натуральных чисел:
squares = [x ** 2 for x in range(1, 11)]

#Словарь с порядковыми номерами дней недели:
weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdays_dict = {day: index + 1 for index, day in enumerate(weekdays)}

#Множество тегов библиотек в нижнем регистре:
tags = {tag.lower() for tag in ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]}

