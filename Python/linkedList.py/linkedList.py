# Implementacao Classica de uma LinkedList

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self,value):
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('empty list')
        
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data

        current = self.head
        while current.next != self.tail:
            current = current.next
        
        data = self.tail.data 
        current.next = None
        self.tail = current
        self.size -= 1
        return data
    
    def remove(self, key):
        if self.is_empty():
            raise IndexError('empty list')
        
        if self.head.data == key:
            data = self.head.data
            self.head = self.head.next
            if self.head is None: 
                self.tail = None
            self.size -= 1
            return data
        

        current = self.head
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            raise ValueError(f'{key} not found')

        prev.next = current.next

        if current == self.tail:
            self.tail = prev

        self.size -= 1
        return current.data
    
    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current.data
            current = current.next
        
        raise ValueError(f'{key} not found')

    def middle_node(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
    
    def reverse_list(self):
        reverseList = None
        current = self.head

        while current:
            nextNode = current.next
            current.next = reverseList
            reverseList = current
            current = nextNode
        
        self.tail = self.head
        self.head = reverseList

    def __len__(self):
        return self.size
    
