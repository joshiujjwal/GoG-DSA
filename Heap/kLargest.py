import math
class Heap:
    def __init__(self):
        self.arr = []
        self.size = 0
    def left(self, index):
        if 2 * index + 1 in range(0,self.size):
            return 2 * index + 1
        return -1
    def right(self, index):
        if 2 * index + 2 in range(0,self.size):
            return 2 * index + 2
        return -1
    def parent(self, index):
        if math.floor((index-1)/2) in range(0,self.size):
            return math.floor((index-1)/2)
        else:
            return -1
    def insertMin(self,key):
        if key in self.arr:
            return 
        else:
            self.arr.append(key)
            self.size +=1
            i = self.size - 1
            while(i!=0 and self.arr[self.parent(i)]>self.arr[i]):
                self.arr[self.parent(i)], self.arr[i] = self.arr[i],self.arr[self.parent(i)]
                i=self.parent(i)
    def heapify(self, index):
        if self.size == 0 or index < 0 or index >= self.size:
            return
        else:
            smallest = index
            if self.left(index) < self.size and self.arr[self.left(index)] < self.arr[smallest]:
                smallest = self.left(index)
            if self.right(index) < self.size and self.arr[self.right(index)] < self.arr[smallest]:
                smallest = self.right(index)
            if smallest != index:
                self.arr[smallest], self.arr[index] = self.arr[index], self.arr[smallest]
                self.heapify(smallest) 

    def extractMin(self):
        if self.size ==0:
            return
        else:
            self.arr[0],self.arr[self.size-1] = self.arr[self.size-1],self.arr[0]
            res = self.arr.pop(self.size - 1)
            self.size-=1
            self.heapify(0)
            return res

def kLargest(arr,k):
    if len(arr) == 0 or k < 1 or k > len(arr):
        return
    else:
        i = 0
        h = Heap()
        for j in range(0,k):
            h.insertMin(arr[j])
        i = i + k
        while(i<len(arr)):
            if arr[i] > h.arr[0]:
                h.extractMin()
                h.insertMin(arr[i])
            i+=1
    return h.arr

if __name__ == "__main__":
    h = Heap()
    arr = [3, 2, 1, 7, 8, 9]
    k = 6
    print(kLargest(arr,k))