# определяем словарь
alias_dict = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
              6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
# размер считываемого буфера
buff_len = 6


# обработка числа
def number_handler(s):
    cut_str = s[2:]
    for index, n in enumerate(cut_str):
        if int(n) % 2 != 0:
            if index % 2 == 0:
                print(n)
            else:
                print(alias_dict[int(n)])


# работа с файлом
with open('workfile', 'r') as f:
    buff = ''
    buff = f.read(buff_len)
    while buff:

        buff = f.read(buff_len)
        if buff and buff[1] == '3':
            number_handler(buff)

print('конец программы')