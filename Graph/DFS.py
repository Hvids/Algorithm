class Vartex:
    def __init__(self, name):
        self.__name = name
        self.__brachs = []
        self.__color = ''
        self.__p = ''
        # метки времени
        self.__distance = 0
        self.__finaly = 0

    def DFS_VISIT(self, time):
        time = time + 1
        self.__distance = time
        self.__color = 'GRAY'
        for i in range(0, len(self.__brachs)):
            if self.__brachs[i].getColor() == 'WHITE':
                self.__brachs[i].setP(self)
                 time = self.__brachs[i].DFS_VISIT(time)
        self.__color = 'BLACK'
        time = time + 1
        self.__finaly = time
        return time

    def getLengthBranchs(self):
        return len(self.__brachs)

    def getColor(self):
        return self.__color

    def setP(self, p):
        self.__p = p
    def setColor(self, color):
        self.__color = color

    def addBranch(sefl, branch):
        self.__brachs.append(branch)

    def setDistance(self, d):
        self.__distance = d

    def setFinaly(self, f):
        self.__finaly = f


class Graph:
    def __init__(self):
        self.__vartexs = []

    def DFS(sefl):
        # первая веришина счиатется стартовой
        for i in range(0,len(self.__vartexs)):
            sefl.__vartexs[i].setColor('WHITE')
            self.__vartexs[i].setP(None)
        time = 0
        for i in range(0,len(self.__vartexs)):
            if self.__vartexs[i].getColor() == 'WHITE':
                time = self.__vartexs[i].DFS_VISIT(time)
    def addVartex(sefl, vartex):
        self.__vartexs.append(vartex)
