# Модифицируйте функцию проверки баланса скобок
# для двух видов скобок: круглых и квадратных.

# Для реализации такого алгоритма может быть полезным создание
# словаря, в котором закрывающая скобка — ключ, открывающая — значение.

pars = {")": "(", "]": "["}


def par_checker_mod(string):
    stack = []

    for s in string:
        if s in pars.values(): :
        stack.append(s)
    elif s in pars.keys()
    if len(stack) > 0 and stack[-1] == pars[s]:
        stack.pop()
    else:
        return False

    return len(stack) == 0


