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
        if index < 0 or index >= self.size or 2 * index + 2 >= self.size:
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
        self.size +=1
        i = self.size - 1
        while(i != 0 and self.arr[self.parent(i)] > self.arr[i]):
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)
    # assuming only index node violating property
    def heapify(self, index):
        if self.size == 0 or index < 0 or index >= self.size:
            return
        smallest = index
        if self.right(index) < self.size and self.arr[self.right(index)] < self.arr[smallest]:
            smallest = self.right(index)
        if self.left(index) < self.size and self.arr[self.left(index)] < self.arr[smallest]:
            smallest = self.left(index)
        if smallest!= index:
            self.arr[index],self.arr[smallest] = self.arr[smallest],self.arr[index]
            self.heapify(smallest)         

        


if __name__ == "__main__":
    h = Heap()
    h.insertMin(20)
    h.insertMin(25)
    h.insertMin(30)
    h.insertMin(35)
    h.insertMin(40)
    h.insertMin(56)
    h.insertMin(15)
    h.insertMin(100)
    h.insertMin(5)
    h.arr[0] = 90
    print(h.arr)
    h.heapify(0)
    print(h.arr)