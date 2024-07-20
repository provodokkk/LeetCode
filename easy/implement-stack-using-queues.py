# Time Complexity: O(1)

class MyStack:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst += [x]

    def pop(self) -> int:
        val = self.lst[-1]
        del self.lst[-1]

        return val

    def top(self) -> int:
        return self.lst[-1]

    def empty(self) -> bool:
        return not self.lst


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()