import sys


class Budget:
    def __init__(self, value):
        self.money = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if value <= 0:
            print("You are out of money!")
            raise sys.exit()
        self.__money = value
