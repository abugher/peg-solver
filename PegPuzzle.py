#!/usr/bin/python3


import copy

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
                line = line + " "
            for y in range(0, max + 1):
                x = max - y
                if True == self.rows[x][y]:
                    line = line + "x "
                else:
                    line = line + "o "
            print(line)
        return True

    def move(self, xy, direction):
        [x, y] = xy
        if not True == self.rows[x][y]:
            return False
        match direction:
            case "pluck":
                if True == self.rows[x][y]:
                    self.rows[x][y] = False
                return True
            case "upRight":
                [newX, newY] = self.upRight(self.upRight([x, y]))
                [middleX, middleY] = self.upRight([x, y])
            case "upLeft":
                [newX, newY] = self.upLeft(self.upLeft([x, y]))
                [middleX, middleY] = self.upLeft([x, y])
            case "downRight":
                [newX, newY] = self.downRight(self.downRight([x, y]))
                [middleX, middleY] = self.downRight([x, y])
            case "downLeft":
                [newX, newY] = self.downLeft(self.downLeft([x, y]))
                [middleX, middleY] = self.downLeft([x, y])
            case "right":
                [newX, newY] = self.right(self.right([x, y]))
                [middleX, middleY] = self.right([x, y])
            case "left":
                [newX, newY] = self.left(self.left([x, y]))
                [middleX, middleY] = self.left([x, y])
            case _:
                return False
        if 0 > newX or 0 > newY or 4 < newX + newY:
            return False
        if True == self.rows[newX][newY]:
            return False
        if False == self.rows[middleX][middleY]:
            return False

        self.rows[x][y] = False
        self.rows[middleX][middleY] = False
        self.rows[newX][newY] = True

        return True
    
    def solve(self, parentHistory = [], all = False, output = False):
        solutions = []
        #print("DEBUG:  output:  '" + output + "'")
        #print("DEBUG:  all:  '" + str(all) + "'")
        match len(parentHistory):
            case 0:
                for x in range(0, self.size):
                    if 0 < len(solutions) and not True == all:
                        break
                    for y in range(0, self.size - x):
                        if 0 < len(solutions) and not True == all:
                            break
                        newPuzzle = copy.deepcopy(self)
                        if not newPuzzle.move([x, y], "pluck"):
                            return False
                        for solution in newPuzzle.solve(parentHistory = [[x, y, "pluck"]], all = all, output = output):
                            if 0 < len(solutions) and not True == all:
                                break
                            solutions.append(solution)
            case 14:
                solutions.append(parentHistory)
                if True == output:
                    print()
                    newPuzzle = Puzzle()
                    newPuzzle.replay(parentHistory)
                    self.summarize(parentHistory)
            case _:
                for x in range(0, self.size):
                    if 0 < len(solutions) and not True == all:
                        break
                    for y in range(0, self.size - x):
                        if 0 < len(solutions) and not True == all:
                            break
                        for direction in [ "upRight", "upLeft", "downRight", "downLeft", "right", "left" ]:
                            if 0 < len(solutions) and not True == all:
                                break
                            newPuzzle = copy.deepcopy(self)
                            if newPuzzle.move([x, y], direction):
                                newHistory = copy.deepcopy(parentHistory)
                                newHistory.append([x, y, direction])
                                for solution in newPuzzle.solve(parentHistory = newHistory, all = all, output = output):
                                    solutions.append(solution)
                                    if not True == all:
                                        break
        return solutions

    def replay(self, history):
        newPuzzle = copy.deepcopy(self)
        for step in history:
            [x, y, direction] = step
            newPuzzle.display()
            if not newPuzzle.move([x, y], direction):
                return False
        newPuzzle.display()

    def summarize(self, history):
        for step in history:
            [x, y, direction] = step
            print(str(x) + "," + str(y) + "," + direction)

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

