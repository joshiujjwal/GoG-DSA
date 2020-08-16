import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def left(self, index):
        if index < 0 or index >= self.size or 2 * index + 1 >= self.size:
            return -1
        else:
            return 2 * index + 1
    
    def right(self, index):
        if index < 0 or index >= self.size or 2*index + 2 >= self.size:
            return -1
        else:
            return 2 * index + 2

    def parent(self, index):
        if index < 0 or index >= self.size or math.floor((index-1)/2) < 0:
            return -1
        else:
            return math.floor((index-1)/2)

    def insertMin(self, key):
        if key in self.arr:
            return 
        self.arr.append(key)
        self.size+=1
        i = self.size - 1
        while(i !=0 and self.arr[self.parent(i)] > self.arr[i]):
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def heapify(self, index):
        if index < 0 or index >= self.size or self.size == 0:
            return
        else:
            smallest = index
            if self.right(index) < self.size and self.arr[smallest] > self.arr[self.right(index)]:
                smallest = self.right(index)
            if self.left(index) < self.size and self.arr[smallest] > self.arr[self.left(index)]:
                smallest = self.left(index)
            if index!=smallest:
                self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
                self.heapify(smallest)


    def extractMin(self):
        if self.size <= 0:
            return
        else:
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
            self.arr.pop(self.size-1)
            self.size -= 1
            self.heapify(0)


if __name__ == "__main__":
    h = Heap()
    h.insertMin(15)
    h.insertMin(5)
    h.insertMin(20)
    h.insertMin(25)
    h.insertMin(40)
    h.insertMin(60)
    h.insertMin(35)
    print(h.arr)
    h.extractMin()
    h.extractMin()
    h.extractMin()
    print(h.arr)

    