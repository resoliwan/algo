import turtle


class Maze:
    def __init__(self, mazeFileName):
        self.rowSize = 0
        self.colSize = 0
        self.map = []
        mazefile = open(mazeFileName)
        self.t = turtle(shape='turtle')
        setup(width=600, height=600)

        for rowIdx, row in enumerate(mazeFile):
            self.rowSize = rowIdx
            for colIdx, col in enumerate(row):
                self.colSize = len(row)
                if col == 'S':
                    self.startRow = rowIdx
                    self.startCol = colIdx
            self.map.append(list(row))






Maze('./recursion/maze.map')
