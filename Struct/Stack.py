class Stack:
    def __init__(self):
        self.__stack = []
        self.__top = -1

    def epmpty(self):
        return self.__top == -1

    def push(self, x):
        self.__top = self.__top + 1
        self.__stack.append(x)

    def pop(self):
        if self.epmpty():
            print('underflow')
        else:
            self.__top = self.__top - 1
            return self.__stack[self.__top + 1]

    def printStack(self):
        print(self.__stack)
        print(self.__top)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    print(s.pop())
