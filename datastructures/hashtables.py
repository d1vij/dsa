from typing import Any

class NestedArrayHashTable:
    """Hash collision handled using nested arrays"""

    def __init__(self, size: int) -> None:
        self.MAXSIZE = size
        self.__array = [[] for _ in range(self.MAXSIZE)]

    def hash(self, key: str):
        return sum(ord(char) for char in key) % self.MAXSIZE

    def __setitem__(self, key, value):
        hash_index = self.hash(key)

        # hash collision using nested tuples within an array

        # checking if value for the already exists ?
        for idx, elm in enumerate(self.__array[hash_index]):
            if elm[0] == key and len(elm) == 2:

                # key exists
                self.__array[hash_index][idx] = (
                    key,
                    value,
                )  # self.__array[hash_index] is of type tuple
                return

        # at this point, the key doesnt exist at that particular hash_index
        self.__array[hash_index].append((key, value))

    def __getitem__(self, key) -> Any:
        hash_index = self.hash(key)
        for elm in self.__array[hash_index]:

            if elm[0] == key:
                return elm[1]

        return None  # key not found

    def __delitem__(self, key):
        hash_index = self.hash(key)

        for idx, elm in enumerate(self.__array[hash_index]):
            if elm[0] == key:
                del self.__array[hash_index][idx]
                return

        raise KeyError("Key not found ", key)

    def __str__(self):
        return "\n".join(f"{k} : {v}" for values in self.__array for k, v in values)

    def values(self):
        return self.__array


class HashTable:
    """Hash Collision handled using Linked Lists"""

    def __init__(self, size: int) -> None:
        self.MAXSIZE = size
        self.__array = [LinkedList() for _ in range(self.MAXSIZE)]

    def hash(self, key: str):
        return sum(ord(char) for char in key) % self.MAXSIZE

    def __setitem__(self, key, value):
        hash_index = self.hash(key)

        # checking if value for the key already exists ? and modifying inplace
        curr = self.__array[hash_index].head
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        # key wasnt there in any node
        self.__array[hash_index].insert_at_end(key, value)

    def __getitem__(self, key):
        hash_index = self.hash(key)

        curr = self.__array[hash_index].head
        if(curr is None): return None # for safety, ideally shouldnt occur

        while(curr is not None):
            if(curr.key == key):
                return curr.value
            curr= curr.next

        return None
    def __delitem__(self, key):
        hash_index = self.hash(key)

        if self.__array[hash_index] is None: return None  # for safety, ideally shouldnt occur

        self.__array[hash_index].remove_by_key(key)
        raise KeyError("Key not found ", key)

    def __str__(self):
        return "\n".join(str(ll) for ll in self.__array)
    
    def values(self):
        return self.__array


from typing import Iterable, Optional


class Node:
    def __init__(self, key, value, next) -> None:
        self.key = key
        self.value = value
        self.next: Node = next


class LinkedList:
    def __init__(self, values: Optional[Iterable] = None):
        self.head = None

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
            outStr += f"({curr.key}, {curr.value}) --> "
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

    def insert_at_end(self, key, value):

        if self.head is None:  # linked list is empty
            self.head = Node(key, value, None)
            return

        lastNode = self.__get_last_node()
        lastNode.next = Node(key, value, next=None)

    # index based operations
    
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

        # skip and dereference the next node (& sends it for gc)
        curr.next = (curr.next).next

    def __get_last_node(self) -> Node:
        # O(n)
        if self.head is None:
            raise ValueError("Linked list is empty")
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        return curr


    def find_index_of_key(self, key):
        """returns first occurance index of passed value, -1 if not found"""
        if self.head == None:
            raise ValueError("Linked list is empty")
        curr = self.head
        index = 0
        while curr is not None:
            index += 1
            if curr.key == key:
                return index
            curr = curr.next

        return -1

    def remove_by_key(self, key) -> None:
        """search for the first occurance of value and remove that particular node from linked list"""

        index = self.find_index_of_key(key)
        if index == -1:
            raise ValueError("Search value not present in this linked list")
        self.remove_at(index)
