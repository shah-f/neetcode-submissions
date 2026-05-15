class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [None] * (capacity)
        self.cap = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.cap:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        popped = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return popped

    def resize(self) -> None:
        self.cap *= 2
        arrNew = [None] * self.cap
        for i in range(self.size):
            arrNew[i] = self.arr[i]
        self.arr = arrNew

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap
