def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)


assert average_num([2, 4, 6, 8, 10, 12]) == 7.0
assert average_num([-2, -4, -6, -8,-10, -12]) == -7.0
assert average_num([1.2, 3, 9.5, 5, 51]) == 13.94
assert average_num([7]) == 7.0
assert average_num([1, '2', 'shmiga', 4, 5]) == "Bad request"
assert average_num(['one', 'two', 'three']) == "Bad request"
assert average_num(['one', 2, 3, 4]) == "Bad request"
assert average_num([2.1, 3.2, 4.3, 5.4, 6.5]) == 4.3