#!/usr/bin/python3

from math import sqrt
from sys import stdin, stderr

def main():
    try:
        A = float(stdin.readline())

        sqrt_A = sqrt(A)

        with open("output.txt", "w") as f:
            f.write(str(sqrt_A))

    except ValueError:
        print("Некорректный ввод!", file=stderr)

    except Exception as e:
        print(f"Ошибка: {e}", file=stderr)

if __name__ == "__main__":
    main()