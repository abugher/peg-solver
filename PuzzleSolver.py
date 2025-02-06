#!/usr/bin/python3

class Puzzle:
    def __init__(self):
        self.rows = []
        self.size = 5
        for x in range(0, self.size):
            self.rows.append([])
            for y in range(0, self.size - x):
                self.rows[x].append(True)
    
    def display(self):
        for max in reversed(range(0, self.size)):
            line = ""
            for i in range(0, self.size - max):
                #line = line + "     "
                line = line + " "
            for y in range(0, max + 1):
                x = max - y
                if True == self.rows[x][y]:
                    #line = line + "[" + str(x) + ", " + str(y) + "]     "
                    line = line + "x "
                else:
                    #line = line + "-----     "
                    line = line + "o "
            print(line)
        return True

    def pluck(self, xy):
        [x, y] = xy
        if 0 > x or 0 > y or 4 < (x + y):
            return False
        self.rows[x][y] = False
        return True

    def move(self, xy, direction):
        [x, y] = xy
        if not True == self.rows[x][y]:
            print("Starting peg empty:  [" + str(x) + ", " + str(y) + "]")
            return False
        match direction:
            case 'upRight':
                [newX, newY] = self.upRight(self.upRight([x, y]))
                [middleX, middleY] = self.upRight([x, y])
            case 'upLeft':
                [newX, newY] = self.upLeft(self.upLeft([x, y]))
                [middleX, middleY] = self.upLeft([x, y])
            case 'downRight':
                [newX, newY] = self.downRight(self.downRight([x, y]))
                [middleX, middleY] = self.downRight([x, y])
            case 'downLeft':
                [newX, newY] = self.downLeft(self.downLeft([x, y]))
                [middleX, middleY] = self.downLeft([x, y])
            case 'right':
                [newX, newY] = self.right(self.right([x, y]))
                [middleX, middleY] = self.right([x, y])
            case 'left':
                [newX, newY] = self.left(self.left([x, y]))
                [middleX, middleY] = self.left([x, y])
            case '_':
                return False
        if 0 > newX or 0 > newY or 4 < newX + newY:
            print("New hole out of range:  [" + str(newX) + ", " + str(newY) + "]")
            return False
        if True == self.rows[newX][newY]:
            print("New hole occupied:  [" + str(newX) + ", " + str(newY) + "]")
            return False
        if False == self.rows[middleX][middleY]:
            print("Middle peg empty:  [" + str(middleX) + ", " + str(middleY) + "]")
            return False

        self.rows[x][y] = False
        self.rows[middleX][middleY] = False
        self.rows[newX][newY] = True

        return True

    def upRight(self, xy):
        [x, y] = xy
        return [x + 1, y]
    
    def upLeft(self, xy):
        [x, y] = xy
        return [x, y + 1]

    def downRight(self, xy):
        [x, y] = xy
        return [x, y - 1]

    def downLeft(self, xy):
        [x, y] = xy
        return [x - 1, y]

    def right(self, xy):
        [x, y] = xy
        return [x + 1, y - 1]

    def left(self, xy):
        [x, y] = xy
        return [x - 1, y + 1]

