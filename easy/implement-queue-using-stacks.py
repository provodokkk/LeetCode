# Time Complexity: O(1) - (push, peek, empty)
# Time Complexity: O(n) - (pop)

class MyQueue:

    def __init__(self):
        self.lst = []

    def push(self, x: int) -> None:
        self.lst += [x]

    def pop(self) -> int:
        return self.lst.pop(0)

    def peek(self) -> int:
        return self.lst[0]

    def empty(self) -> bool:
        return not self.lst


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()