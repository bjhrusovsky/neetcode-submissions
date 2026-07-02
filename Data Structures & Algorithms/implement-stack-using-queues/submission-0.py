from collections import deque

class MyStack:

    def __init__(self):
        self.__myQueue = deque()

    def push(self, x: int) -> None:
        self.__myQueue.append(x)

    def pop(self) -> int:
        return self.__myQueue.pop()

    def top(self) -> int:
        return self.__myQueue[-1]

    def empty(self) -> bool:
        if len(self.__myQueue) > 0:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()