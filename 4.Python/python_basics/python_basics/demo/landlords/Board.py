'''
牌信息
'''
class Board:
    def __init__(self, number, pattern):
        self.number = number
        self.pattern = pattern

    def __str__(self):
        return f"{self.number} {self.pattern}"

    def __repr__(self):
        return f"{self.number} {self.pattern}"