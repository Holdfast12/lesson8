#!/usr/bin/python3
"""Написать класс “animals” (животные), который включает общие признаки и поведения животных.
От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих.
От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
"""

class Animals:
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

class Mammals(Animals):
    pass

class Human(Mammals):
    def __init__(self, weight, height, age, name, gender):
        super().__init__(weight, height, age)
        self.name = name
        self.gender = gender

    def voice(self):
        print(f'Привет, я {self.name}')

class Cat(Mammals):
    def __init__(self, breed):
        #порода
        self.breed = breed
    def voice(self):
        print('мяу')

class Dog(Mammals):
    def __init__(self, breed):
        #порода
        self.breed = breed
    def voice(self):
        print('гав')

Vasya = Human(90, 180, 40, 'Вася', 'male')

print(Vasya.name)