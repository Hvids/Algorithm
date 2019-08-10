class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.rigth = None
        self.p = None
        self.color = None


class RBTree:
    def __init__(self):
        self.__root = None

    def insert(self, z):
        y = None
        x = self.__root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.rigth
        z.p = y
        if y == None:
            self.__root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.rigth = z
        z.left = None
        z.rigth = None
        z.color = 'RED'
        self.__InertFixup(z)

    def delete(self, z):
        y = z
        x = ''
        y_original_color = y.color
        if z.left == None:
            x = z.rigth
            self.__Transplant(z, z.rigth)
        elif z.rigth == None:
            x = z.left
            self.__Transplant(z, z.left)
        else:
            y_original_color = y.color
            x = y.rigth
            if y.p == z:
                x.p = y
            else:
                self.__Transplant(y,y.rigth)
                y.rigth = z.rigth
                y.rigth.p = y
            self.__Transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
        if y_original_color == 'BLACK':
            self.__DeleteFixup(x)

    def __DeleteFixup(self,x):
        while x == None and x.color == 'BLACK':
            if x == x.p.left:
                w = x.p.rigth
                if w.color = 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.__LeftRotate(x.p)
                    w = x.p.rigth
                if w.left.color == 'BLACK' and w.rigth.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                elif w.rigth.color == 'BLACK':
                    w.left.color = 'BLACK'
                    w.color = 'RED'
                    self.__RigthRotate(w)
                    w = w.p.rigth
                w.color = x.p.color
                x.p.color = 'BLACK'
                w.rigth.color = 'BLACK'
                self.__LeftRotate(x.p)
                x = self.__root
            else:
                w = x.p.left
                if w.color = 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.__LeftRotate(x.p)
                    w = x.p.left
                if w.rigth.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                elif w.left.color == 'BLACK':
                    w.rigth.color = 'BLACK'
                    w.color = 'RED'
                    self.__RigthRotate(w)
                    w = w.p.left
                w.color = x.p.color
                x.p.color = 'BLACK'
                w.left.color = 'BLACK'
                self.__LeftRotate(x.p)
                x = self.__root
    def __treeMinimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def __treeMaximum(self, node):
        while node.rigth != None:
            node = node.rigth
        return node

    def __InertFixup(self, z):
        while z.p.color = 'RED':
            if z.p == z.p.p.left:
                y = z.p.p.rigth
                if y.color == 'RED':
                    z.p.color = 'BLACK'
                    y.color = 'BLACK'
                    z.p.p.color = 'RED'
                    z = z.p.p
                elif z == z.p.rigth:
                    z = z.p
                    self.__LeftRotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.__RigthRotate(z.p.p)
            else:
                if z.p == z.p.p.rigth:
                    y = z.p.p.left
                    if y.color == 'RED':
                        z.p.color = 'BLACK'
                        y.color = 'BLACK'
                        z.p.p.color = 'RED'
                        z = z.p.p
                    elif z == z.p.left:
                        z = z.p
                        self.__LeftRotate(z)
                        z.p.color = 'BLACK'
                        z.p.p.color = 'RED'
                        self.__RigthRotate(z.p.p)
        self.__root.color = 'BLACK'

    def __Transplant(self, u, v):
        if u.p == None:
            self.__root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.rigth = v
        v.p = u.p

    def __RigthRotate(z):
        y = x.left
        x.left = y.rigth
        if y.rigth ! = None
        y.rigth.p = x
        y.p = x.p
        if x.p = None:
            self.__root = y
        elif x == x.p.rigth:
            x.p.rigth = y
        else:
            x.p.left = y
        y.rigth = x
        x.p = y

    def __LeftRotate(self, x):
        y = x.rigth
        x.rigth = y.left
        if y.left ! = None
        y.left.p = x
        y.p = x.p
        if x.p = None:
            self.__root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.rigth = y
        y.left = x
        x.p = y
