
try:
    age=int(input("Сколько тебе лет?"))
    if age>100 or age<=0:
        raise ValueError("Тебе не может быть столько лет!")
    print(f"Тебе {age} лет")
except ValueError:
    print("Неправильный возраст!")