a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
set1, set2 = set(a), set(b)
print(set1)
print(set2)
print("Union: ", set1.union(set2))
print("Intersection: ", set1.intersection(set2))
print("Difference: ", set1.difference(set2))
print("Difference: ", set2.difference(set1))
print("Symmetric_difference: ", set1.symmetric_difference(set2))