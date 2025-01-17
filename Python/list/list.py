# Implementacao Classica de uma Lista(list).

class List:
    def __init__(self, initial_size):
        self.capacity = initial_size
        self.data = [0] * self.capacity
        self.size = 0 

    def _resize(self):
        new_capacity = self.capacity * 2
        new_data = [None] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        if self.size == self.capacity:
            self._resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                removed_value = self.data[i]
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = 0
                self.size -= 1
                return removed_value
        raise ValueError(f"{value} not found")
    
    def pop(self):
        if self.size == 0:
            raise IndexError("empty list")
        
        value = self.data[self.size - 1]
        self.data[self.size - 1] = 0
        self.size -= 1
        return value

    def __len__(self):
        return self.size
