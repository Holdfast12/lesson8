#!/usr/bin/python3
"""Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
"""
import time

#функция 
def logging(func):
    def wrapper():
        func()
        with open('')
    return wrapper

@logging
def another_func():
    print('Это еще одна функция')

another_func()