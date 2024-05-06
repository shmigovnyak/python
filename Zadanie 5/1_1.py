import random

def randomelements(lst):
    return random.sample(lst, 2)

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]

print(randomelements(list_el))
