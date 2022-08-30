L = ['Hello', 'world']
M = L # копируется не сам список, а его id
#
print(M is L)       # True
# поэтому, при изменении M изменяется и L:
M.append('!')
print(L)
# ['Hello', 'world', '!']
#Чтобы избежать такого поворота событий, список нужно КОПИРОВАТЬ.
M = L.copy()
print(M is L)       # False
print(' '.join(L))