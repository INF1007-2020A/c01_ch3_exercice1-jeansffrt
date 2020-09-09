#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def square_root(number: int) -> float:
    square_rooted = math.sqrt(number) # La fonction math.sqrt(i) retourne la racine carrée du nombre i
    return square_rooted

def square(number: int) -> int:
    squared = math.pow(number, 2) # La fonction math.pow(i,2) retourne i à la puissance 2
    return squared


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
