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
    def insertMin(self,key,i,j):
        self.arr.append([key,i,j])
        self.size +=1
        i = self.size - 1
        while(i!=0 and self.arr[self.parent(i)][0]>self.arr[i][0]):
            self.arr[self.parent(i)], self.arr[i] = self.arr[i],self.arr[self.parent(i)]
            i=self.parent(i)
    
    
    def heapify(self, index):
        if self.size == 0 or index < 0 or index >= self.size:
            return
        else:
            smallest = index
            if self.left(index) < self.size and self.arr[self.left(index)][0] < self.arr[smallest][0]:
                smallest = self.left(index)
            if self.right(index) < self.size and self.arr[self.right(index)][0] < self.arr[smallest][0]:
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

def mergeKSorted(arr,k):
    h = Heap()
    i = 0
    for j in range(0,k):
        h.insertMin(arr[j][i], j, i)
    while(h.size):
        res = h.extractMin()
        print(res[0],end=" ")
        if res[2]+1 < len(arr[res[1]]):
            h.insertMin(arr[res[1]][res[2]+1], res[1], res[2]+1)

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,8],[9,12,19]]
    mergeKSorted(arr,3)
