"""
С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Каждая из матриц B, C, D, E имеет вид:
     4
  3     1
     2
Вариант 2:
Формируется матрица "F" следующим образом: если в "С" количество положительных элементов в четных столбцах
в области 2 больше, чем количество отрицательных элементов в нечетных столбцах в области 4, то поменять в "С"
симметрично области 1 и 3 местами, иначе "С" и "Е" поменять местами несимметрично. При этом матрица А не меняется.
После чего вычисляется выражение: (F + A) * AT – K * F. Выводятся по мере формирования "А", "F" и
все матричные операции последовательно.
"""

from math import ceil
import random as r


def print_matrix(matrix):  # функция вывода матрицы
    matrix1 = list(map(list, zip(*matrix)))
    for i in range(len(matrix1)):
        c = len(max(list(map(str, matrix1[i])), key=len))
        matrix1[i] = [f'{elem:{c+1}d}' for elem in matrix1[i]]
    matrix1 = list(map(list, zip(*matrix1)))
    for row in matrix1:
        print(*row)


try:
    n = int(input('Введите число N больше 4: '))
    k = int(input('Введите число K: '))
    while n < 5:
        n = int(input('Введите число N больше 4: '))

    o_cnt = p_cnt = 0
    middle_n = ceil(n / 2)  # Середина матрицы
    A = [[r.randint(-10, 10) for i in range(n)] for j in range(n)]  # Задаём матрицу A
    AT = [[0 for i in range(n)] for j in range(n)]  # Заготовка под транспонированную матрицу А
    F = A.copy()  # Задаём матрицу F
    KF = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат умножения матрицы F на коэффициент K
    FA = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат сложение матрицы F и А
    FAAT = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат умножения матрицы FA на матрицу AT
    result = [[0 for i in range(n)] for j in range(n)]  # Заготовка под результат вычитания двух матриц

    for i in range(n):  # Транспонируем матрицу А
        for j in range(n):
            AT[i][j] = A[j][i]

    print('\nМатрица А:')
    print_matrix(A)
    print('\nТранспонированная А:')
    print_matrix(AT)

    # Выделяем матрицы E C
    if n % 2 == 1:
        E = [A[i][middle_n - 1:n] for i in range(middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n - 1, n)]
    else:
        E = [A[i][middle_n:n] for i in range(0, middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n, n)]

    for i in range(middle_n):  # Считаем в 2 области в чётных столбцах в матрице "С" кол-во положительных эл.
        for j in range(middle_n):
            if (i + j + 1) >= middle_n and (i >= j) and (j + 1) % 2 == 0:
                if C[i][j] > 0:
                    p_cnt += 1

    for i in range(middle_n):  # Считаем кол-во отрицательных элементов в зоне 4 в нечётных столбцах в матрице "C"
        for j in range(middle_n):
            if (i <= j) and ((i + j + 1) <= middle_n) and ((j + 1) % 2 == 1):
                if C[i][j] < 0:
                    o_cnt += 1

    if p_cnt > o_cnt:
        print(f'\nВ матрице "C" количество положительных элементов в четных столбцах в области 2({p_cnt})')
        print(f'больше чем количество отрицательных элементов в нечетных столбцах в области 4({o_cnt})')
        print('поэтому симметрично меняем местами области 1 и 3 в С.')
        for i in range(middle_n):
            for j in range(0, middle_n):
                if (i + j + 1) <= middle_n and i >= j:
                    C[i][j], C[(middle_n - i) - 1][(middle_n - j) - 1] = C[(middle_n - i) - 1][(middle_n - j) - 1], C[i][j]  # Симметрично меняем местами области 1 и 3 в "С"

        if n % 2 == 1:
            for i in range(middle_n - 1, n):
                for j in range(0, middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]  # Перезаписываем С
        else:
            for i in range(middle_n, n):
                for j in range(0, middle_n):
                    F[i][j] = C[i - middle_n][j]  # Перезаписываем С
    else:
        print(f'\nВ матрице "C" количество положительных элементов в четных столбцах в области 2({p_cnt})')
        print(f'меньше чем количество отрицательных элементов в нечетных столбцах в области 4({o_cnt}) или равно ей')
        print('поэтому несимметрично меняем местами подматрицы C и E:')
        C, E = E, C
        if n % 2 == 1:
            for i in range(middle_n - 1, n):  # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
            for i in range(middle_n):  # Перезаписываем Е
                for j in range(middle_n - 1, n):
                    F[i][j] = E[i][j - (middle_n - 1)]
        else:
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]
            for i in range(0, middle_n):
                for j in range(middle_n, n):
                    F[i][j] = E[i][j - middle_n]

    # F + A
    for i in range(n):
        for j in range(n):
            FA[i][j] = F[i][j] + A[i][j]  # Вычисляем сумму двух матриц

    # K * F
    for i in range(n):
        for j in range(n):
            KF[i][j] = k * F[i][j]  # Производим умножение матрицы F на коэффициент

    # FA * AT
    for i in range(n):
        for j in range(n):
            for m in range(n):
                FAAT[i][j] += FA[i][m] * AT[m][j]  # Производим умножение матрицы FA на матрицу AT

    # FAAT - KF
    for i in range(n):
        for j in range(n):
            result[i][j] = FAAT[i][j] - KF[i][j]  # Вычисляем разность двух матриц

    # Вывод всех операций
    print('\nМатрица F:')
    print_matrix(F)
    print('\nРезультат К * F:')
    print_matrix(KF)
    print('\nРезультат F + A:')
    print_matrix(FA)
    print('\nРезультат (F + A) * AT:')
    print_matrix(FAAT)
    print('\nРезультат (F + A) * AT – K * F:')
    print_matrix(result)
    print('\nРабота программы завершена.')
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')
