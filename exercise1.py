#!/usr/bin/python3
"""Написать класс “animals” (животные), который включает общие признаки и поведения животных.
От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих.
От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.
"""

class Animals:
    """Класс животные"""
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age = age

    def move(self):
        """Метод животных для перемещения в пространстве"""
        print(f'*тело этого животного перемещается в пространстве*')


class Mammals(Animals):
    """Класс млекопитающие.
    Параметр limbs - тип конечностей.
    """
    def __init__(self, weight, height, age, limbs, gender):
        super().__init__(weight, height, age)
        self.limbs = limbs
        self.gender = gender

    def feed_milk(self):
        """Метод млекопитающих для кормления молоком"""
        if self.gender == 'female':
            print(f'*млекопитающее начинает кормить молоком*')
        else:
            print('функция кормления молоком доступна только для female')
 

class Human(Mammals):
    """Класс человек"""
    def __init__(self, weight, height, age, limbs, name, gender):
        super().__init__(weight, height, age, limbs, gender)
        self.name = name
        self.gender = gender

    def voice(self):
        """Метод человека для разговора"""
        print(f'Привет, я {self.name}')


class Cat(Mammals):
    """Класс кошка"""
    def __init__(self, weight, height, age, limbs, name, gender, breed, color):
        super().__init__(weight, height, age, limbs, gender)
        self.name = name
        self.breed = breed
        self.color = color

    def voice(self):
        """Метод кошки для разговора"""
        print('мяу')


class Dog(Mammals):
    """Класс собака.
    Параметр breed - порода
    """
    def __init__(self, weight, height, age, limbs, name, gender, breed, color):
        super().__init__(weight, height, age, limbs, gender)
        self.name = name
        self.breed = breed
        self.color = color
        
    def voice(self):
        """Метод собаки для разговора"""
        print('гав')


if __name__ == '__main__':

    ivan = Mammals(1500, 150, 7, 'hooves', 'male')
    ivan.move()
    ivan.feed_milk()

    petr = Human(90, 180, 30, 'hands', 'Petr', 'male')
    petr.move()
    petr.feed_milk()

    anna = Human(95, 165, 25, 'hands', 'Anna', 'female')
    anna.feed_milk()

    vasya = Cat(5, 20, 7, 'paws', 'vasya', 'male', 'british', 'gray')
    vasya.voice()

    zhuchka = Dog(10, 60, 10, 'paws', 'Zhuchka', 'female', 'dvor', 'black')
    zhuchka.voice()