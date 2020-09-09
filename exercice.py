#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def square_root(number: int) -> float:
    square_rooted = math.sqrt(number) # La fonction math.sqrt() retourne la racine carrée du nombre passé en entré
    return square_rooted

def square(number: int) -> int:
    squared = math.pow(number, 2)
    return squared


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
