from typing import Iterable, Optional


class Node:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next: Node = next


class LinkedList:
    def __init__(self, values: Optional[Iterable] = None):
        self.head = None
        if values is not None:
            self.set_values(values)

    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"

        outStr = ""
        curr = self.head
        while curr != None:
            outStr += str(curr.value) + " --> "
            curr = curr.next
        outStr += "end"
        return outStr

    def to_list(self):
        if self.head is None:
            return []

        outList = []
        curr = self.head
        while curr is not None:
            outList.append(curr.value)
            curr = curr.next
        return outList

    # changing values of nodes

    def set_values(self, values: Iterable):
        """sets linked list to values array"""
        self.head = None
        for val in values:
            self.insert_at_end(val)

    def set_value_at(self, index: int, value):
        """changes value of node at the given index"""

        if index >= len(self):
            raise ValueError("Index out of range", index)
        if self.head == None:
            raise ValueError("List is empty")

        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.value = value

    # position based operations

    def insert_at_begining(self, value):
        newNode = Node(value, self.head)
        self.head = newNode

    def insert_at_end(self, value):

        if self.head is None:  # linked list is empty
            self.head = Node(value, None)
            return

        lastNode = self.__get_last_node()
        lastNode.next = Node(value=value, next=None)

    # index based operations

    def insert_at(self, index: int, value):
        if index < 0:
            raise ValueError("Index cannot be lesser than 0")

        length = len(self)
        if index >= length:
            raise ValueError(f"Index cannot be greater than self's length :{length}")

        if index == 0:
            self.insert_at_begining(value)
            return

        assert isinstance(self.head, Node)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        next_node = curr.next
        curr.next = Node(value, next_node)

        return

    def remove_at(self, index: int):
        if index < 0:
            raise ValueError("Index cannot be negative")
        length = len(self)
        if index >= length:
            raise ValueError("Index cannot be greater than self's length of ", length)

        if index == 0:
            self.head = self.head.next  # type: ignore
            return

        assert isinstance(self.head, Node)

        curr = self.head
        # getting node at index
        for _ in range(index - 1):
            curr = curr.next

        curr.next = (curr.next).next

    def __get_last_node(self) -> Node:
        if self.head is None:
            raise ValueError("Linked list is empty")
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr

    # problems

    def find_index(self, value):
        """returns first occurance index of passed value, -1 if not found"""

        if self.head == None:
            raise ValueError("Linked list is empty")

        curr = self.head
        index = 0

        while curr is not None:
            index += 1

            if curr.value == value:
                return index
            curr = curr.next

        return -1

    def insert_after_value(self, search_value, insert_value):
        """search for first occurance of search_value and insert a new node having value insert_value after it"""
        index = self.find_index(search_value)

        if index == -1:
            raise ValueError("Search value not present in this linked list")

        self.insert_at(index, insert_value)

    def remove_by_value(self, value):
        """search for the first occurance of value and remove that particular node from linked list"""

        index = self.find_index(value)
        if index == -1:
            raise ValueError("Search value not present in this linked list")
        self.remove_at(index - 1)
