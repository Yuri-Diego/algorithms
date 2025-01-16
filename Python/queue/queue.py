# Implementacao Classica de uma Fila(queue) Circular.


class Queue:
    def __init__(self, max_length):
        self.items = [0] * max_length
        self.max_length = max_length
        self.front = 0
        self.pointer = 0
        self.size = 0

    def enqueue(self, value):
        if self.pointer >= self.max_length:
            raise IndexError("Full queue")
        
        self.items[self.pointer] = value
        self.pointer = (self.pointer + 1) % self.max_length
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.max_length
        self.size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty queue")
        
        return self.items[self.front]
    
    def is_empty(self):
        return self.size == 0
    
    def size(self):
        return self.size