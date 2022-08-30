from divide_line import line
import math
#
matrix = [
    [4,5,6,7,3,4,5,6,2,8],
    [0,1,5,8,6,9,3,4,8],
    [7,6,3,1,0,4,5,8],
    [1,0,3,0,5,0,8],
    [4,5,8,6,9,4],
    [0,1,8,6,3],
    [7,5,8,6],
    [1,2,5],
    [8,5],
    [8]
]

for row in matrix:
    # print('\n')
    for col in row:
        print(col, end=' ')
    print()

line()

# число Фибоначчи. Попробую самостоятельно соорудить эту рекурсию...

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(19))

print(1+1+2+3+5+8+13+21+34+55+89+144+233+377+610+987+1597+2584+4181)



