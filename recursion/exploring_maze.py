import turtle
import importlib

OBSTATCLE = '+'
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
                    self.startCol = colIdx
            self.map.append(list(row))
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.xTranslate = 0
        self.yTranslate = self.rowSize 
        self.wn.setworldcoordinates(0, 0, +self.colSize, +self.rowSize)

    def drawMaze(self):
        # self.wn.tracer(0)
        for y in range(self.rowSize):
            for x in range(self.colSize):
                print('x: {}, y: {}, val: {}'.format(x, y, self.map[y]))
                if self.map[y][x] == OBSTATCLE:
                    self.drawCenteredBox(x, y, 'orange')

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



m = Maze('./recursion/maze.map')
m.drawMaze()
