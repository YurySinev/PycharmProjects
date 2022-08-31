"""
Здесь содержится описание вашего модуля
"""

import os
import sys

import requests

import my_stack

MAIN_CONSTANT = 3.14159265358


def main():
    print(MAIN_CONSTANT)
    some_func()


def some_func():
    print(help(os))
    print(help(sys))
    print(help(requests))
    print(help(my_stack))


if __name__ == '__main__':
    main()

