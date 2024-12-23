import random

print('Угадайте число от 1 до 100')
user_number = 0
random_number = random.randint(1, 100)
while user_number != random_number:
    user_number = int(input('Введите число: '))
    if user_number > random_number:
        print('Ваше число больше того, что загадано')
    elif user_number < random_number:
        print('Ваше число меньше того, что загадано')
print('Отличная интуиция! Вы угадали число :)')
# Bla-bla 2
