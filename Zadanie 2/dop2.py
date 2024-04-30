set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}


merged_set = set1.union(set2)
final_set = merged_set.union(set3)

not_in_set = (set1 & set2) | (set1 & set3) | (set2 & set3)

print(merged_set)
print(final_set)
difference = final_set - not_in_set

print("Элементы, которые не вошли в множества:", not_in_set)

print("Разница всех элементов множества и списка:", difference)