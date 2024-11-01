#!/usr/bin/python3

from random import randint
from sys import stdin, stderr

def main():
    try:
        A = float(stdin.readline())

        B = randint(-10, 10)

        ratio = A / B

        print(ratio)

    except ZeroDivisionError:
        print("Деление на ноль!", file=stderr)

    except ValueError:
        print("Некорректный ввод!", file=stderr)

if __name__ == "__main__":
    main()