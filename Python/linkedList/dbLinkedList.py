# Implementacao Classica de uma Doubly LinkedList.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self.size += 1

    def remove_from_front(self):
        if not self.head:
            raise IndexError('empty list')
        removed_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return removed_value
    
    def remove_from_end(self):
        if not self.head:
            raise IndexError('empty list')
        removed_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
        return removed_value
    
    def remove_by_key(self, key):
        if not self.head:
            raise IndexError('empty list')
        
        if self.head.value == key:
            data = self.head.value
            self.head = self.head.next
            if self.head is None: 
                self.tail = None
            self.size -= 1
            return data
        
        if self.tail.value == key:
            data = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.size-= 1
            return data


        current = self.head 
        while current:
            if current.value == key:
                current.prev.next = current.next
                current.next.prev = current.prev
                self.size -= 1
                return current.value

            current = current.next

        raise ValueError(f'{key} not found')
    
    def contains(self, key):
        current = self.head

        while current:
            if current.value == key:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size