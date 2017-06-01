import turtle
import importlib

OBSTACLE = '+'
TRIED = '.'
PART_OF_PATH = '0'
DEAD_END = '-'

class Maze:
    def __init__(self, mazeFileName):
        importlib.reload(turtle)
        self.rowSize = 0
        self.colSize = 0
        self.map = []
        mazeFile = open(mazeFileName, 'r')
        for rowIdx, row in enumerate(mazeFile):
            self.rowSize = rowIdx + 1
            row = row[:-1]
            for colIdx, col in enumerate(row):
                self.colSize = len(row)
                if col == 'S':
                    self.startRow = rowIdx
                    self.startColumn = colIdx
            self.map.append(list(row))
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.xTranslate = 0
        self.yTranslate = self.rowSize - 1
        self.wn.setworldcoordinates(0, 0, +self.colSize, +self.rowSize)

    def drawMaze(self):
        self.wn.tracer(0)
        for y in range(self.rowSize):
            for x in range(self.colSize):
                x, y = self.translate(x, y)
                # print('x: {}, y: {}, val: {}'.format(x, y, self.map[y]))
                if self.map[y][x] == OBSTACLE:
                    self.drawCenteredBox(x, y, 'orange')
        self.t.color('black')
        self.t.fillcolor('black')
        self.wn.update()
        self.wn.tracer(1)

    def translate(self, x, y):
        return (x, self.yTranslate - y)

    def moveTurtle(self, x, y):
        x, y = self.translate(x, y)
        self.t.up()
        self.t.setheading(self.t.towards(x, y))
        self.t.goto(x, y)

    def dropBreadCrumb(self, color):
        self.t.dot(10, color)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x, y)
        self.t.color('orange')
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()

        for i in range(4):
            self.t.forward(1)
            self.t.right(90)

        self.t.end_fill()
    
    def updatePosition(self, row, col, val=None):
        if val:
            self.map[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'       
        else:
            color = None

        if color:
            self.dropBreadCrumb(color)
    
    def isExit(self, row, col):
        return (row == 0 or row == self.rowSize - 1 or
                col == 0 or col == self.colSize - 1)


def searchForm(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    if maze.map[startRow][startColumn] == OBSTACLE:
        return False

    if maze.map[startRow][startColumn] == TRIED or maze.map[startRow][startColumn] == DEAD_END:
        return False

    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startColumn, TRIED)

    found = searchForm(maze, startRow-1, startColumn) or \
            searchForm(maze, startRow+1, startColumn) or \
            searchForm(maze, startRow, startColumn-1) or \
            searchForm(maze, startRow, startColumn+1)

    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)

    return found


m = Maze('./recursion/maze.map')
m.drawMaze()
searchForm(m, m.startRow, m.startColumn)
