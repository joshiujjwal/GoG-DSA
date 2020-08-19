import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def right(self, index):
        if 2 * index + 1 in range(self.size):
            return 2 * index + 1
        else:
            return -1
    def left(self, index):
        if 2 * index + 2 in range(self.size):
            return 2 * index + 2
        else:
            return -1
    def parent(self, index):
        if math.floor((index-1)/2) in range(self.size):
            return math.floor((index-1)/2)
        else:
            return -1
    def insertMin(self, key):
        if key in self.arr:
            return 
        else:
            self.arr.append(key)
            self.size+=1
            i = self.size -1
            while(i!=0 and self.arr[self.parent(i)]>self.arr[i]):
                self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
                i = self.parent(i)
    def heapify(self, index):
        if index < 0 or self.size == 0 or index >= self.size:
            return
        else:
            smallest = index
            if self.right(index) < self.size and self.arr[self.right(index)] < self.arr[smallest]:
                smallest = self.right(index)
            if self.left(index) < self.size and self.arr[self.left(index)] < self.arr[smallest]:
                smallest = self.left(index)              
            if smallest != index:
                self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
                self.heapify(smallest)
    def extractMin(self):
        if self.size == 0:
            return
        else:
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
            self.arr.pop(self.size-1)
            self.size-= 1
            self.heapify(0)


if __name__ == "__main__":
    h = Heap()
    arr = [1,3,4,7,32,2,8]
    sum_val = 1
    count = 0
    for i in arr:
        h.insertMin(i)
    while h.size > 0 and h.arr[0] <= sum_val:
        sum_val -= h.arr[0]
        h.extractMin()
        count+=1
    print(count)

            