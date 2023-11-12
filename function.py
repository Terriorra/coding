import os
import sys

from random import randint
from random import sample
from random import choice

sign_hor = '═'
sign_vert = '║'
LINE_LEN = 90


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


path = resource_path('about')
with open(path, 'r', encoding='utf-8') as f:
    about = f.read().split('\n\n\n')

path = resource_path('support')
with open(path, 'r', encoding='utf-8') as f:
    support = f.read().split('\n')

path = resource_path('susses')
with open(path, 'r', encoding='utf-8') as f:
    susses = f.read().split('\n')

path = resource_path('singular.txt')
with open(path, 'r', encoding='utf-8') as f:
    nouns = f.read().split('\n')


cup = about[7]

# Создадим словарь
dict_noun = {}
for word in nouns:
    if len(word) not in dict_noun:
        dict_noun[len(word)] = [word]
    else:
        dict_noun[len(word)].append(word)

words_nouns = []
for i in nouns:
    if len(i) == len(set(i)):
        words_nouns.append(i)


def print_text(text, len_string):
    s = [f" {(len_string - 2) * sign_hor} ", f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}"]

    for line in text:
        if len(line) + 4 < len_string:
            s.append(f"{sign_vert} {line}{(len_string - len(line) - 4) * ' '} {sign_vert}")
        else:
            s += cut_string(line, len_string)
    s.append(f"{sign_vert}{(len_string - 2) * ' '}{sign_vert}")
    s.append(f" {(len_string - 2) * sign_hor} ")

    return s


def cut_string(text, len_string):
    s = []

    text = text.split(' ')
    lines = []
    now = ''
    for i in text:
        if len(now + ' ' + i) < len_string - 4:
            now += ' ' + i
        else:
            lines.append(now)
            now = i
    lines.append(now)

    for line in lines:
        s.append(f"{sign_vert} {line}{(len_string - 4 - len(line)) * ' '} {sign_vert}")

    return s


class Quest:
    def __init__(self, text, ans):
        self.text = text
        self.ans = ans


def create_srt(n: int = 5) -> (str, list[str]):
    """
    Создание строки из n слов
    :param n: количество слов
    :return:
    """

    a = randint(3, 5)

    text = 'Выписанные слова - '
    words = []
    for i in range(a, a + n):
        words.append(choice(dict_noun[i]))

    words = sample(words, n)

    text += f'{", ".join(words)}.'

    return text, words


def cod_n(weight: int = 8, n: int = 5):
    """

    :param weight:
    :return:
    """

    text = 'В кодировке '
    sent, words = create_srt(n)

    word = choice(words)
    n_del = len(word)

    match weight:
        case 8:
            text += f"{choice(['КОИ-8', 'Windows-1251', 'UTF-8', 'ASCII'])} каждый символ кодируется 8 битами."
            n_del = (n_del + 2) * 8
        case 16:
            text += f"{choice(['Unicode', 'UTF-16'])} каждый символ кодируется 16 битами."
            n_del = (n_del + 2) * 16
        case 32:
            text += f"{choice(['UTF-32', 'Unicode'])} каждый символ кодируется 32 битами."
            n_del = (n_del + 2) * 32

    text += f'\n\nНаписанное предложение:\n{sent}\n\n'

    d = choice([f'{int(n_del / 8)} байт', f'{n_del} бит'])

    text += (f'Ученик удалил из предложения одно слово, а также лишние запятую и пробел — два пробела '
             f'не должны идти подряд. При этом размер нового предложения в данной кодировке оказался '
             f'на {d} меньше, чем размер исходного предложения. '
             f'Напишите в ответе вычеркнутое название предмета.')

    return Quest(print_text(text.split('\n'), LINE_LEN), word)


def cod_sumd(var):
    lt = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    word = choice(words_nouns)
    while len(word) > 6:
        word = choice(words_nouns)

    letters = list(word) + sample(list(set(lt) - set(word)), randint(1, 3))
    letters = sample(letters, len(letters))

    # Сгенерирую словарь
    cipher_dict = {i: '' for i in letters}

    symbols = ''

    match var:
        case 1:
            symbols = choice(['+~@', '@~*', '+^#', '~#+', '–•', '?€', '?©', 'ΛΩ', '!?'])
            symbols = 10 * symbols
        case 2:
            symbols = 10 * '10'

    ciphers = []
    for i in letters:
        cipher = ''.join(sample(symbols, randint(1, 4)))
        while cipher in ciphers:
            cipher = ''.join(sample(symbols, randint(1, 4)))

        ciphers.append(cipher)
        cipher_dict[i] = ''.join(cipher)

    trans_table = str.maketrans(cipher_dict)

    tabl = [f'{i} : {cipher_dict[i]}' for i in cipher_dict]
    tabl = '\n'.join(tabl)

    text = f'Сообщение было зашифровано кодом. Использовались только буквы, приведенные в таблице:\n{tabl}\n\n'
    text += f'Определите, какое сообщение закодировано в строчке {word.translate(trans_table)}.'

    return Quest(print_text(text.split('\n'), LINE_LEN), word)




def create_count(right):
    s = 'Для продолжения необходимо решить пять задач.'
    s += f'\nОсталось решить {5 - right}'

    return print_text(s.split('\n'), LINE_LEN)


def create_text_1(var, right):
    os.system("CLS")
    text = print_text(about[0].split('\n'), LINE_LEN)
    t = ''
    q = ''
    match var:
        case 1:
            t = print_text(about[1].split('\n'), LINE_LEN)
            q = cod_n(8, randint(3, 10))
        case 2:
            t = print_text(about[2].split('\n'), LINE_LEN)
            q = cod_n(16, randint(3, 10))
        case 3:
            t = print_text(about[3].split('\n'), LINE_LEN)
            q = cod_n(32, randint(3, 10))

    text += t
    text += create_count(right)
    text += q.text

    return text, q


def create_text_2(var, right):
    os.system("CLS")
    text = print_text(about[4].split('\n'), LINE_LEN)
    t = ''
    q = ''
    match var:
        case 1:
            t = print_text(about[5].split('\n'), LINE_LEN)
            q = cod_sumd(1)
        case 2:
            t = print_text(about[6].split('\n'), LINE_LEN)
            q = cod_sumd(2)

    text += t
    text += create_count(right)
    text += q.text

    return text, q
