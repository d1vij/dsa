from typing import Iterable, Optional


class DblNode:
    def __init__(self, value, next, prev) -> None:
        self.value = value
        self.next: DblNode = next
        self.prev: DblNode = prev


class DblLinkedList():
    def __init__(self, values: Optional[Iterable]):
        self.head = None
        if(values):
            self.set_values(values)
            

    def set_values(self, values: Iterable):
        self.head = None
        for value in values:
            self.insert_at_end(value)
            

    def insert_at_end(self, value):
        if(self.head is None):
            self.head = DblNode(value, None, None)
            return
        
        lastNode = self.get_last_node()
        lastNode.next = DblNode(value, None, lastNode)

    def insert_at_begining(self, value):
        if(self.head is None):
            self.head = DblNode(value, None, None)
            return
        
        self.head = DblNode(value, self.head, None)


    def get_last_node(self):
        if(self.head is None): raise ValueError("This Doubly Linked List is empty")

        curr = self.head
        while(curr.next is not None):
            curr = curr.next
        return curr
    
    def print_forward(self):
        curr= self.head
        while(curr is not None):
            print(curr.value)
            curr=  curr.next

    def print_backward(self):
        curr= self.get_last_node()
        while(curr is not None):
            print(curr.value)
            curr = curr.prev
            