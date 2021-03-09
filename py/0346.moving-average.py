class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        from collections import deque

        self.q = deque()
        self.mov = 0
        self.q_size = 0
        self.window_size = size

    def next(self, val: int) -> float:
        self.q.append(val)
        self.q_size += 1
        if self.q_size <= self.window_size:
            self.mov = (self.mov * (self.q_size - 1) + val)/self.q_size
        else:
            self.mov = self.mov - self.q.popleft() / self.window_size + val / self.window_size
        return self.mov

obj = MovingAverage(3)
param_1 = obj.next(1)
param_2 = obj.next(10)
param_3 = obj.next(3)
param_4 = obj.next(5)


print(param_1)
print(param_2)
print(param_3)
print(param_4)