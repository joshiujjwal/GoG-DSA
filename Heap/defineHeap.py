import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def left(self, index):
        if self.size == 0 or index < 0 or index * 2 + 1 >= size:
            return -1
        else:
            return self.arr[2 * index + 1]
    def right(self, index):
        if self.size == 0 or index < 0 or index * 2 + 2 >= size:
            return -1
        else:
            return self.arr[2 * index + 2]
    def parent(self, index):
        if self.size == 0 or index < 0 or math.floor((i-1)/2) < 0:
            return -1
        else:
            return math.floor((i-1)/2)
    