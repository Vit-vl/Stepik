def matr(n):
    if n == 1:
        print('Матрешечка')
    else:
        print('Верх матрешки = ', n)
        matr(n - 1)
        print('Низ матрешки = ', n)
matr(5)
