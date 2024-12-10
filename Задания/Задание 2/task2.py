#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def generate_matrix(rows, cols, min_value, max_value):
    matrix = []
    for _ in range(rows):
        row = [random.randint(min_value, max_value) for _ in range(cols)]
        matrix.append(row)
    return matrix


def main():
    try:
        rows = int(input("Введите количество строк: "))
        cols = int(input("Введите количество столбцов: "))
        min_value = int(input("Введите минимальное значение: "))
        max_value = int(input("Введите максимальное значение: "))
        matrix = generate_matrix(rows, cols, min_value, max_value)
        print("Сгенерированная матрица:")
        for row in matrix:
            print(row)
    except ValueError:
        print("Ошибка: Введите целое число.")


if __name__ == "__main__":
    main()