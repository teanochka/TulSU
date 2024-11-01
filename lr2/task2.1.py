#!/usr/bin/python3

import re
from sys import stderr, stdin, argv


def validate_name(name: str):
    if not name:
        raise Exception("Name can't be empty.")
    if not bool(re.match(r"^[A-Za-z]+$", name)):
        raise Exception("Name must consist of latin letters")
    if not name[0].isupper():
        raise Exception(f"Name {name} needs to start in uppercase")

def greet_name(name):
    try:
            validate_name(name)
            print(f"Nice to see you {name}!")
    except Exception as e:
        print(f"Error: {str(e)}", file=stderr)
def main():
    if len(argv) > 1:
        try:
            with open(argv[1], "r") as f:
                names = [line.strip() for line in f]
                for name in names:
                    greet_name(name)
        except FileNotFoundError:
            print(f"Error: File {argv[1]} not found.", file=stderr)
    else:
        while True:
            try:
                print("What's your name?")
                name = str((stdin.readline()))
                greet_name(name)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}", file=stderr)


if __name__ == "__main__":
    main()
