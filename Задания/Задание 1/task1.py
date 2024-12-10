#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    a = input('Первое значение: ')
    b = input('Второе значение: ')

    try:
        a = float(a)
        b = float(b)
        summa = a + b
        print(f'Результат: {summa}')
    except ValueError:
        summa = str(a) + str(b)
        print(f'Результат: {summa}')
    else:
        print(f'Все верно, вы ввели оба числа {a} и {b}')
    finally:
        print('Программа завершена.')