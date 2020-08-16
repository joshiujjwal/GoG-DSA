import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def left(self, index):
        if self.size == 0 or index < 0 or 2 * index + 1 >= size:
            return -1
        else:
            return 2 * index + 1
    def right(self, index):
        if self.size == 0 or index < 0 or 2 * index + 2 >= size:
            return -1
        else:
            return 2 * index + 2
    def parent(self, index):
        if self.size == 0 or index < 0 or math.floor((index-1)/2) < 0:
            return -1
        else:
            return math.floor((index-1)/2)


    def insertMin(self, key):
        self.arr.append(key)
        self.size +=1
        i = self.size - 1
        while i!=0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

if __name__ == "__main__":
    h = Heap()
    h.insertMin(20)
    h.insertMin(25)
    h.insertMin(30)
    h.insertMin(35)
    h.insertMin(40)
    h.insertMin(80)
    h.insertMin(32)
    h.insertMin(100)
    h.insertMin(70)
    h.insertMin(60)
    print(h.arr)





