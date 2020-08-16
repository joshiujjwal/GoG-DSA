import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def left(self, index):
        if 2 * index + 1  in range(0, self.size):
            return 2 * index + 1
        else:
            return -1
    def right(self, index):
        if 2 * index + 2 in range(0, self.size):
            return 2 * index + 2
        else:
            return -1
    def parent(self, index):
        if math.floor((index-1)/2) in range(0, self.size):
            return math.floor((index-1)/2)
        else:
            return -1 
    def insertMin(self, key):
        if key in self.arr:
            return
        self.arr.append(key)
        self.size += 1
        i = self.size-1
        while(i!=0 and self.arr[self.parent(i)]>self.arr[i]):
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
    def decreaseKey(self,index, key):
        if self.size == 0 or index < 0 or index>=self.size:
            return
        else:
            self.arr[index] = key
            while(index!=0 and self.arr[self.parent(index)] > self.arr[index]):
                self.arr[index], self.arr[self.parent(index)] = self.arr[self.parent(index)], self.arr[index]
                index = self.parent(index)


if __name__ == "__main__":
    h = Heap()
    h.insertMin(20)
    h.insertMin(15)
    h.insertMin(25)
    h.insertMin(30)
    h.insertMin(35)
    h.insertMin(40)
    h.insertMin(50)
    print(h.arr)
    h.decreaseKey(4,5)
    print(h.arr)


    
