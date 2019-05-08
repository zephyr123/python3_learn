from random import randint
"""骰子"""
class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        i = 0
        while i < 10:
            x = randint(1, 6)
            print(x)
            i += 1
    def roll_die_ten(self):
        i = 0
        while i < 10:
            print(randint(1,10))
            i += 1

zhangsan = Die()
# zhangsan.roll_die()
zhangsan.roll_die_ten()