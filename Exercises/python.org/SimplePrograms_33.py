import random

guesses_made = 0

name = input('Привет! Как тебя звать-то?\n')

number = random.randint(1, 20)
print ('ОК, {0}, я задумал число от 1 до 20.'.format(name))

while guesses_made < 6:

    guess = int(input('Попробуй угадать: '))

    guesses_made += 1

    if guess < number:
        print ('Меньше моего числа.')

    if guess > number:
        print ('Больше моего числа.')

    if guess == number:
        break

if guess == number:
    print ('Неплохо, {0}! С {1} попытки ты все ж таки угадал число!'.format(name, guesses_made))
else:
    print ('Нет. Я задумал число {0}'.format(number))