import math

class Heap:
    def __init__(self):
        self.arr=[]
        self.size=0
    def left(self, index):
        if 2 * index + 1 in range(0,self.size):
            return 2 * index + 1
        else:
            return -1
    def right(self,index):
        if 2 * index + 2 in range(0,self.size):
            return 2 * index + 2
        else:
            return -1
    def parent(self, index):
        if math.floor((index-2)/2) in range(0,self.size):
            return math.floor((index-1)/2)
        else:
            return -1 
    def insertMin(self, key):
        if key in self.arr:
            return
        self.arr.append(key)
        self.size +=1
        i = self.size - 1
        while(i!=0 and self.arr[self.parent(i)] > self.arr[i]):
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)
    def decreaseKey(self, index, key):
        if self.size == 0 or index >= self.size or index < 0:
            return
        else:
            self.arr[index] = key
            while(index!=0 and self.arr[self.parent(index)] < self.arr[index]):
                self.arr[index], self.arr[self.parent(index)] = self.arr[index], self.arr[self.parent(index)]
                index = self.parent(index)
    
    def heapify(self, index):
        if self.size == 0 or index < 0 or index >= self.size:
            return
    
    def extractMin(self):
        if self.size == 0:
            return 
        else:
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
            self.arr.pop(self.size-1)
            self.size-=1
            self.heapify(0) 