from random import choice

from function import create_text_1
from function import create_text_2
from function import support
from function import susses
from function import cup

name = input('Приветствую тебя. Как к тебе обращаться? ')
print(f'Приятно познакомиться, {name}, здесь две темы c пятью разделами.')

input('Нажми enter, когда будешь готов...')

for var in [1, 2, 3]:
    right = 0
    while right < 5:
        t, q = create_text_1(var, right)
        for i in t:
            print(i)
        ant = input('\nВведи свой ответ: ').strip().lower()

        if q.ans == ant:
            print(f'Верно, {name}! ')
            print(choice(susses))
            right += 1
        else:
            print(f'Не верно! Верный ответ {q.ans}.')
            print(f'{name}, {choice(support)}')

        input('Нажми enter, когда будешь готов...')

print('Первый раздел завершён!')
print(f'Ты прошёл половину пути, {name}.')
print(f'Текущая оценка 3, чтобы получить оценку выше пройди ещё два раздела.')
input('Нажми enter, когда будешь готов...')

for var in [1, 2]:
    right = 0
    while right < 5:
        t, q = create_text_2(var, right)
        for i in t:
            print(i)
        ant = input('\nВведи свой ответ: ').strip().lower()

        if q.ans == ant:
            print(f'Верно, {name}! ')
            print(choice(susses))
            right += 1
        else:
            print(f'Не верно! Верный ответ {q.ans}.')
            print(f'{name}, {choice(support)}')

        input('Нажми enter, когда будешь готов...')

    if var == 1:
        print('Текущая оценка 4.')
        print(f'Хорошая работа, {name}. Для отличной оценки нужно пройти ещё один раздел.')
        input('Нажми enter, когда будешь готов...')

print(f'Всё пройдено, {name}.')
print(choice(susses))
print()

print(cup)

input('Нажми enter, когда будешь готов...')
input()
input()
input()
