"""Вариант 2.
Натуральные числа, не превышающие 1 000 000, у которых вторая слева цифра равна 3.
Выводит на экран нечетные цифры стоящие в числе справа от этой 3.
Цифры, стоящие на нечетных местах (в числе), выводятся прописью. """

m = []
chisla = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simvols = [' ', '!', '?', '.', ',', '\n', '', ':', '-', ';', '"', ')', '(']
buffer_len = 1
work_buffer = ''


def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
         '8': 'восемь', '9': 'девять'}
    return z[x]


with open('test.txt') as f:
    buffer = f.read(buffer_len)
    if not buffer:
        print('Файл пустой.')
        quit()
    while buffer:
        while buffer not in simvols:
            work_buffer += buffer
            buffer = f.read(buffer_len)
        if len(work_buffer) > 0:
            flag = True
            for i in range(len(work_buffer)):
                if work_buffer[i] not in chisla:
                    flag = False
            if flag and len(work_buffer) > 1:
                l = ''
                k = ''
                if work_buffer[1] == '3' and int(work_buffer) <= 1_000_000:
                    m += [int(work_buffer)]
                    for j in work_buffer[2:]:
                        if int(j) % 2 == 1:
                            l += str(j)
                    k = work_buffer[::2]
                    u = ''
                    for o in range(len(str(k))):
                        g = slovo(str(k)[o])
                        u += g + ' '
                    print('Вывод:')
                    print(f'Нечетные цифры стоящие в числе справа от 3:\n{l}')
                    print(f'Цифры, стоящие на нечетных местах:\n{u}\n')
        work_buffer = ''
        buffer = f.read(buffer_len)

if not m:
    print('В файле нет подходящих значений.')