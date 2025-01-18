# Implementacao Classica de uma MinHeap(Priority Queue)
# implementada para rebalancear e ordenar um array de elementos
# ao adicionar (insert) e remover o elemento minimo (pop_min)

class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return (2 * index) + 1
     
    def _right_child(self, index):
        return (2 * index) + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _heapify_up(self, index):
        if index == 0:
            return
        
        parent_index = self._parent(index)

        if self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        size = len(self.heap)

        left = self._left_child(index)
        right = self._right_child(index)
        
        smallest_index = index

        if left < size and self.heap[left] < self.heap[smallest_index]:
            smallest_index = left
        if right < size and self.heap[right] < self.heap[smallest_index]:
            smallest_index = right

        if smallest_index != index:
            self._swap(index, smallest_index)
            self._heapify_down(smallest_index)

    def _swap(self, index, reverse):
        self.heap[index], self.heap[reverse] = self.heap[reverse], self.heap[index]

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError('empty heap')
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

