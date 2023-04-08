"""Вариант 2.
Натуральные числа, не превышающие 1 000 000, у которых вторая слева цифра равна 3.
Выводит на экран нечетные цифры стоящие в числе справа от этой 3.
Цифры, стоящие на нечетных местах (в числе), выводятся прописью. """

import re

m = []


def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
         '8': 'восемь', '9': 'девять'}
    return z[x]


f = open('test.txt')
buffer = f.readline().split()
if not buffer:
    print('Файл пустой.')
    quit()
else:
    while True:
        if not buffer:
            break
        for i in buffer:
            l = ''
            k = ''
            work_buffer = re.findall(r'\b[0-9]3[0-9]{0,4}\b', i)
            if work_buffer:
                m += [int(work_buffer[0])]
                for j in work_buffer[0][2:]:
                    if int(j) % 2 == 1:
                        l += str(j)
                k = work_buffer[0][::2]
                u = ''
                for o in range(len(str(k))):
                    g = slovo(str(k)[o])
                    u += g + ' '
                print('Вывод:')
                print(f'Нечетные цифры стоящие в числе справа от 3:\n{l}')
                print(f'Цифры, стоящие на нечетных местах:\n{u}\n')
        buffer = f.readline().split()

if not m:
    print('В файле нет подходящих значений.')
