import random

class MineField():
    def __init__(self, width:int=10, height:int=10, mines:int=10):
        self.width: int = width
        self.height: int = height
        self.mines: int = mines

        self.field: list = [['.' for _ in range(self.width)] for _ in range(self.height)]

    def CreateField(self):
        mine_count = 0
        while mine_count < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.field[y][x] != '*':
                self.field[y][x] = '*'
                mine_count += 1

    def PrintField(self):
        for row in self.field:
            print(" ".join(row))

if __name__ == "__main__":
    minefield = MineField(width=10, height=10, mines=10)
    minefield.CreateField()
    minefield.PrintField()
