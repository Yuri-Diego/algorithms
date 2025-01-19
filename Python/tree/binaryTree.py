# Implementacao de uma Binary Tree (arvore binaria) com metodos:
# Busca Binaria Com complexicadade O(log n)
# Visualizacao inOrder, preOrder e PostOrder
# Metodos de Caminhos: BFS(Buscar em Largura) e DFS(Busca em Profundidade)

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else: 
            self._insert_recursive(value, self.root)
    def _insert_recursive(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)

    # ------------ BUSCA BINARIA ------------ #
    def search(self, value):
        return self._search_recursive(self.root, value)
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


    def preOrder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    def _preOrder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inOrder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    def _inOrder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def postOrder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    def _postOrder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


    def bfs(self, value):
        if self.root is None:
            return False
    
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            print(node.value)
            if node.value == value:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return False
    

    def dfs(self,value):
        return self._dfs_recursive(self.root, value)
    def _dfs_recursive(self, node, value):
        if node: 
            print(node.value)
        if node is None:
            return False
        if node.value == value:
            return True
        if self._dfs_recursive(node.left, value):
            return True
        if self._dfs_recursive(node.right, value):
            return True


    def height(self):
        return self._height_recursive(self.root)
    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)
    

    def find_min(self):
        current = self.root
        while current and current.left:
            current = current.left
        return current.value if current else None

    def find_max(self):
        current = self.root
        while current and current.right:
            current = current.right
        return current.value if current else None

# ------------ TESTES ------------ #

# tree = BinaryTree()
# tree.insert(5)
# tree.insert(3)
# tree.insert(1)
# tree.insert(10)
# tree.insert(15)
# tree.insert(7)
# tree.insert(20)

# print(tree.search(3))
# print(tree.search(4))

# print("PreOrder:", tree.preorder())
# print("InOrder:", tree.inorder())
# print("PosOrder:", tree.postorder())

# print("BFS", tree.bfs(20))
# print("DFS", tree.dfs(20))
