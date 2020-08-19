import math
class heap:
    def __init__(self):
        self.arr = []
        self.size = 0
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
    def parent(self,index):
        if math.floor((index-1)/2) in range(0,self.size):
            return math.floor((index-1)/2)
        return -1
    def insertMin(self,key):
        if key in self.arr:
            return
        else:
            self.arr.append(key)
            self.size+=1
            i = self.size - 1
            while(i!=0 and self.arr[self.parent(i)]>self.arr[i]):
                self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
                i = self.parent(i)
    def insertMax(self,key):
        if key in self.arr:
            return
        else:
            self.arr.append(key)
            self.size +=1
            i = self.size - 1
            while(i!=0 and self.arr[self.parent(i)]<self.arr[i]):
                self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
                i = self.parent(i)
    def minheapify(self, index):
        if self.size == 0:
            return
        else:
            smallest = index
            if self.right(index) < self.size and self.arr[self.right(index)] < self.arr[smallest]:
                smallest = self.right(index)
            if self.left(index) < self.size and self.arr[self.left(index)] < self.arr[smallest]:
                smallest = self.left(index)
            if smallest != index:
                self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
                self.minheapify(smallest)
    def  maxheapify(self,index):
        if self.size == 0:
            return
        else:
            highest = index
            if self.right(index) < self.size and self.arr[self.right(index)] > self.arr[highest]:
                highest = self.right(index)
            if self.left(index) < self.size and self.arr[self.left(index)] > self.arr[highest]:
                highest = self.left(index)
            if highest!=index:
                self.arr[index], self.arr[highest] = self.arr[highest], self.arr[index]
                self.maxheapify(highest)
    
    def extractMin(self):
        if self.size == 0:
            return
        else:
            self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
            res = self.arr.pop(self.size-1)
            self.size-=1
            self.minheapify(0)
            return res
    
    def extractMax(self):
        if self.size == 0:
            return
        else:
            self.arr[0], self.arr[self.size-1] = self.arr[self.size -1], self.arr[0]
            res = self.arr.pop(self.size -1)
            self.size -=1
            self.maxheapify(0)
            return res
    


if __name__ == "__main__":
    arr = [6,4,8,2,10,1,56,5,7]

    c1 = heap()
    c2 = heap()

    for i in arr:
        if c1.size == c2.size:
            if c1.size > 0 and c2.size > 0 and i > c2.arr[0]:
                c1.insertMax(c2.extractMin())
                c2.insertMin(i)
            else:
                c1.insertMax(i)
            print("Median", c1.arr[0])
        else:
            if c2.size > 0 and i > c2.arr[0] :
                c2.insertMin(c1.extractMax())
                c1.insertMax(i)
            else:
                c2.insertMin(i)
            if c2.size:
                print("Median", (c1.arr[0] + c2.arr[0])/2)


        

