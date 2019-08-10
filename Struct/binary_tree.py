class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.rigth = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.__root = None

# Печать дерева

    def printBinaryTree(self):
        self.__inorderTreeWalk(self.__root, 0)

# Получить под узел по ключу

    def getSubNode(self, key_find):
        return self.__treeSearch(self.__root, key_find)

# Удаление из дерева

    def deleteTree(self, z):
        if z.left == None:
            self.__transplant(z,z.rigth)
        elif z.rigth_high == None:
            self.__transplant(z,z.left)
        else:
            y = self.__treeMinimum(z.rigth)
            if y.p != z:
                self.__transplant(y,y.rigth)
                y.rigth = z.rigth
                y.rigt.p = y
            sefl.__transplant(z,y)
            y.left = z.left
            y.left.p = y


# Вставка в дерево

    def insertTree(self, z):
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
# Предществующий элемент

    def getSuccessor(self,node):
        if node.rigth != None:
            return self.__treeMaximum(node.rigth)
        y = node.parent

        while y != None and x == y.rigth:
            x = y
            y = y.p
        return y

#  Минимум

    def getMinimum(self):
        return self.__treeMinimum(self.__root)

# Максимум

    def getMaximum(self):
        return self.__treeMaximum(sefl.__root)

# Перестройка дерева

    def __transplant(self, u, v):
        if u.p == None:
            self.__root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.rigth = v
        if v != None:
            v.p = u.p

# Максмимум в дереве поиска

    def __treeMaximum(self, node):
        while node.rigth != None:
            node = node.rigth
        return node

# Минимум в дереве прогулка с поиском

    def __treeMinimum(self, node):
        while node.left != None:
            node = node.left
        return node

# Прогулка по дереву с печатью

    def __inorderTreeWalk(self, node, space):
        if node != None:
            self.__inorderTreeWalk(node.left, space + 1)
            for i in range(0, space):
                print('\t', end='')
            print(node.key)
            self.__inorderTreeWalk(node.rigth, space + 1)
# Поиск в дереве

    def __treeSearch(self, node, key_find):
        if node == None or key_find == node.key:
            return node
        if key_find < node.key:
            return self.__treeSearch(node.left, key_find)
        else:
            return self.__treeSearch(node.rigth, key_find)


if __name__ == '__main__':
    tree = BinaryTree()
    node = Node(10)
    tree.insertTree(node)
    node = Node(5)
    tree.insertTree(node)
    node = Node(11)
    tree.insertTree(node)
    node = Node(9)
    tree.insertTree(node)
    tree.printBinaryTree()
    tree.deleteTree(node)
    tree.printBinaryTree()
