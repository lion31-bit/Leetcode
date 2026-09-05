from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)                    # naya element rear me daalo
        for _ in range(len(self.q) - 1):    # baaki sab ko rotate karke
            self.q.append(self.q.popleft()) # front se hata ke rear me daal do
        # ab naya element hamesha front pe aa jayega

    def pop(self) -> int:
        return self.q.popleft()             # sirf front access — legal

    def top(self) -> int:
        return self.q[0]                    # front hi dekho, -1 nahi

    def empty(self) -> bool:
        return len(self.q) == 0