
a = input("Понимает ли клиент доброе слово? Y/N \n" )
if a=='Y' or a=='y':
    print("Обсудите с клиентом все проблемы и вместе найдите решения.")
else:
    print("Вставьте ему пистолет в рот.")
    a = input("Понимает ли теперь клиент доброе слово? Y/N")
    if a=='Y' or a=='y':
        print("Уберите пистолет. Решите все проблемы с клиентом путем их обсуждения.")
    else:
        print("Нажмите на курок.")
