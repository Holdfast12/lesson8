#!/usr/bin/python3
"""Написать класс “Student”, который наследует класс human,
у которого среди прочих признаков есть “Количество сданных дз”.

* Перегрузить операторы сравнения так,
чтобы студенты сравнивались по количеству сданных ими дз.
"""

from exercise1 import Human

class Student(Human):
    def __init__(self, weight, height, age, name, gender, hw_points):
        super().__init__(weight, height, age, name, gender)
        self.hw_points = hw_points
    def __lt__(self, other):
        return self.hw_points < other.hw_points
    def __le__(self, other):
        return self.hw_points <= other.hw_points
    def __eq__(self, other):
        return self.hw_points == other.hw_points

Vasya = Student(100, 180, 50, 'Вася', 'male', 40)
Vova = Student(70, 175, 20, 'Вова', 'male', 30)

print(Vasya.hw_points)
print(Vova.hw_points)
print(Vasya <= Vova)