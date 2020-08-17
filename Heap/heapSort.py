import math
class heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def left(self, index):
        if 2 * index + 1 in range(0, self.size):
            return 2 * index + 1
        else:
            return -1
    def right(self, index):
        if 2 * index + 2 in range(0,self.size):
            return 2 * index + 2
        else:
            return -1
    def parent(self, index):
        if math.floor((index-1)/2) in range(0, self.size):
            return math.floor((index-1)/2)
        else:
            return -1 
    def insertMax(self, key):
        if key in self.arr:
            return
        else:
            self.arr.append(key)
            self.size+=1
            i = self.size-1
            while(i!=0 and self.arr[self.parent(i)] < self.arr[i]):
                self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
                i = self.parent(i)

    def heapify(self, index):
        if index < 0 or index >= self.size or self.size == 0:
            return   
        else:
            highest = index
            if self.left(index) < self.size and self.arr[self.left(index)] > self.arr[highest]:
                highest = self.left(index)
            if self.right(index) < self.size and self.arr[self.right(index)] > self.arr[highest]:
                highest = self.right(index)
            if highest != index:
                self.arr[highest], self.arr[index] = self.arr[index], self.arr[highest]
                self.heapify(highest)

    def heapSort(self):
        if self.size == 0:
            return
        else:
            res = []
            while(self.size>0):
                self.arr[self.size-1], self.arr[0] = self.arr[0], self.arr[self.size-1]
                res.insert(0,self.arr.pop(self.size-1))
                self.size -=1
                self.heapify(0)
        return res

        

if __name__ == "__main__":
    h = heap()
    h.insertMax(12)
    h.insertMax(5)
    h.insertMax(56)
    h.insertMax(78)
    h.insertMax(50)
    h.insertMax(30)
    h.insertMax(25)
    print(h.arr)
    print(h.heapSort())

