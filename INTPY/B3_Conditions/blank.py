print("Что надеть?")

T = int(input("Какая сегодня температура на улице? "))

if (T > 20) and (T < 30):
    rain = str(input("Осадки есть? Yes/No "))
    if rain == "Yes":
        print("Наденьте футболку, шорты и дождевик")
    else:
        print("Наденьте футболку и шорты")
elif T > 0:
    rain = str(input("Осадки есть? Yes/No "))
    if rain == "Yes":
        strong_rain = str(input("Осадки сильные? Yes/No "))
        if strong_rain == "Yes":
            print("Наденьте пальто и резиновые сапоги, и возьмите зонт.")
        else:
            print("Наденьте пальто и дождевик.")
    else:
        print("Наденьте пальто.")
else:
    print("Наденьте пуховик!")