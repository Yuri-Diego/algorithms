# Implementacao do MergeSort, algoritmo de ordenacao muito utilizado em LinkedLists
# Melhor caso (Best case): O(n log n).
# Pior caso (Worst case): O(n log n).

def find_midle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    head = Node()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return head.next

def mergeSort(head):
    if not head or not head.next:
        return head
    
    middle = find_midle(head)
    after_middle = middle.next
    middle.next = None
    left = mergeSort(head)
    right = mergeSort(after_middle)

    sorted_list = merge(left, right)
    return sorted_list

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)

my_list = mergeSort(node_9)
print(my_list)