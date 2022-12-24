#!/usr/bin/python3
"""Написать функцию. Для неё написать декораторы для следующего функционала:
    ◦ логирование выполнения функции;
    ◦ время выполнения функции;
    ◦ замедлить выполнение кода. Ограничить частоту вызова функции.
"""
import time


def logging(func):
    """Декоратор, логирующий выполнение декорируемой функции в файл"""
    def wrapper():
        func()
        with open('log.txt', 'a') as file:
            file.write(f'{time.ctime()} Произошло логируемое выполнение функции\n')
    return wrapper


def timing(func):
    """Декоратор, выводящий затраченное время на выполнение функции"""
    def wrapper():
        start = time.time()
        func()
        print(f'Время выполнения функции составило {time.time() - start} секунд')
    return wrapper


def call_limit(func):
    """Декоратор, не позволяющий вызвать функцию чаще чем раз в 5 секунд
        latency - задержка выполнения в секундах
    """
    latency = 5
    last = [time.time() - latency]
    def wrapper():
        if time.time() - last[0] < latency:
            print('Слишком частый вызов функции')
        else:
            last[0] = time.time()
            func()
    return wrapper



@call_limit
@logging
@timing
def another_func():
    print('Декорируемая функция')

another_func()
time.sleep(6)
another_func()
another_func()
time.sleep(3)
another_func()
