import random


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value if len(value) <= 10 else value[0:10]

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 18:
            self.__age = value
        else:
            raise ValueError

    def __str__(self):
        return f"{self.name} {self.age}"

    def __repr__(self):
        return f"{self.name} {self.age}"


class Student(Person):
    def __init__(self,  name: str, age: int, mid_ball: float):
        super().__init__(name, age)
        self.mid_ball = mid_ball

    @property
    def mid_ball(self):
        return self.__mid_ball

    @mid_ball.setter
    def mid_ball(self, value):
        if 0 < value <= 5.0:
            self.__mid_ball = value
        else:
            raise ValueError

    def __str__(self):
        return f"{self.name} {self.age} {self.mid_ball}"

    def __repr__(self):
        return f"{self.name} {self.age} {self.mid_ball}"


def generate_list(length: int = 10, min_value: int = 0, max_value: int = 9) -> []:
    if length < 0 or max_value <= min_value:
        raise ValueError
    return [random.randint(min_value, max_value) for _ in range(length)]


if __name__ == '__main__':
    S = Student('Иванов', 23, 3.4)
    print(S)
    P = [
        Student('Иванов', 23, 3.7),
        Student('Петров', 28, 2.6),
        Student('Сергеев', 42, 4.4),
        Student('Сидоров', 35, 2.7),
        Student('Олегов', 48, 3.4)
    ]
    print(P)
    P.sort(key=lambda x: x.mid_ball, reverse=True)
    print(P)
    for i in P:
        print(i)
