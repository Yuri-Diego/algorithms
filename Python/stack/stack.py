# Implementacao classica de uma Pilha

class Stack:
    def __init__(self, max_length):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0

    def is_empty(self):
        return self.pointer == 0
    
    def push(self,item):
        if self.pointer >+ self.max_length:
            raise IndexError("Stack full")
        
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty stack.")
        
        self.pointer -= 1
        return self.items[self.pointer]
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Stack")
        
        return self.items[self.pointer - 1]
    
    def size(self):
        return self.pointer