#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max = []

    def Push(self, a):
        if len(self.__stack) == 0:
            self.max.append(a)
        else:
            self.max.append(max(self.max[-1],a))
        self.__stack.append(a)

    def Pop(self):
        # assert(len(self.__stack))
        self.__stack.pop()
        self.max.pop()

    def Max(self):
        return self.max[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
