# В клетке находятся фазаны и кролики. Известно, что у них 35 голов и 94 ноги.
# Узнайте число фазанов и число кроликов.

heads = 35
legs = 94

for r in range(heads + 1):
    for ph in range(heads + 1):
        if (r + ph) != heads or (r * 4 + ph * 2) != 94:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Кроликов: ", r, "Фазанов: ", ph)
