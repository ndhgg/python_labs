"""
1. Пусть дана строка, состоящая из слов, пробелов и знаков препинания.
    На основании этой строки создайте новую (и выведите ее на консоль):
Вариант 4. Содержащую только слова, в которых две последние буквы — «ов».
"""

import re


def run():
    stroke = 'малинов, гессе, гегель, орлов'

    temp = re.findall(r'\w+', stroke)  # Поиск слов в строке
    print(temp)
    s = ''
    for i in temp:
        if re.match(r'\w*ов$', i):  # Поиск слов на "ов"
            s += i + ' '

    print(s)