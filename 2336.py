

class Dog:
    def __init__(self) -> None:
        print('this is a dog')

    def num(self, a: int) -> int:
        return a


a = Dog().num(2)
print(a)
