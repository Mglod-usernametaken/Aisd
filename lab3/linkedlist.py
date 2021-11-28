from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value = None):
        self.value = value
        self.next = None


class LinkedList:
    head: 'Node'
    tail: 'Node'

    def __init__(self, first:Node = Node):
        self.head = first
        self.tail = first

    def __len__(self):
        i = 0
        node = self.head
        while node != None:
            i = i+1
            node = node.next
        return i
        
    def __str__(self):
        string = ""
        node = self.head
        for x in range(len(self)):
            if node.next != None:
                string += str(node.value) + " -> "
            if node.next ==None:
                string += str(node.value)
            node = node.next
        return string

    def append(self, value: Any):
        node = Node(value)
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def node(self, at:int)-> Node:
        seek = self.head
        while at > 0:
            at -= 1
            seek = seek.next
        return seek

    def len(self):
        current = self.head
        sum = 0
        while current.next!=None:
            sum +=1
            current = current.next
        return sum

    def display(self) -> None:
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next

    def push(self, new: Node = Node):
        new_node = new
        new_node.next = self.head
        self.head = new_node

    def pop(self)->Any:
        if self.head == None:
            return
        bye = self.head
        self.head = self.head.next
        return bye.value

    def remove(self, after:Node)->Any:
        former = self.head
        while former != after:
            if former == None:
                return
            former = former.next
        if former.next == None:
            return
        else:
            skipped = former.next
            former.next = skipped.next

    def remove_last(self)->Any:
        if self.head == None:
            return
        else:
            ogon = self.tail
            self.last = self.node(self.__len__() - 2)
            self.tail.next = None
            return ogon


n1 = Node("pierwszy")
n2 = Node("drugi")
n3 = Node("trzeci")

list1 = LinkedList(n1)
list1.head.next = n2
list1.push(n3)
list1.push(Node(444))
print(list1.__len__())
list1.display()
# print(list1.node(0).value)
# print('this', list1.pop())
print('\n')
# list1.remove(n3)
list1.display()
print(list1)

# ----------------------------------------------------------------------------------

class Stack()
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList 

    def __len__(self):
        return len(self._storage)

    def __str__(self)->Any:
        string = ""
        return string

    def push(self, element: Any)-> None:

    def pop(self) -> Any:
        