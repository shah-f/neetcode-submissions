class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.nextNode
        return curr.curr

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if self.head.nextNode is None:
            self.tail = new_node
        self.size+=1

    def insertTail(self, val: int) -> None:
        new_node = Node(val, None)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.nextNode = new_node
            self.tail = new_node
        self.size+=1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        if index == 0:
            self.head = self.head.nextNode
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return True
        curr = self.head
        for _ in range(index-1):
            curr = curr.nextNode
        removed = curr.nextNode
        curr.nextNode = removed.nextNode
        if removed == self.tail:
            self.tail = curr
        self.size-=1
        return True

    def getValues(self) -> List[int]:
        ret = []
        curr = self.head
        while (curr != None):
            ret.append(curr.curr)
            curr = curr.nextNode
        return ret
        
class Node:
    def __init__(self, curr, nextNode):
        self.curr = curr
        self.nextNode = nextNode