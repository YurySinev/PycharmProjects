# Сравните:

a, b = 1, 2
min = a if a < b else b
print(min)  # 1

#вместо

a, b = 1, 2
min = None
if a < b:
    min = a
else:
    min = b
print(min)  # 1

# или
a, b  = 1, 2
print(a,"больше") if a>b  else print(b,"больше")
# 2 больше

# вместо

a, b  = 1, 2
if a > b :
    print(a,"больше")
else:
    print(b,"больше")
# 2 больше