
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_head(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self):
        last = self.tail.prev
        self.remove(last)
        return last

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class LRUCache:
    def __init__(self, capacity):
        self.sequence = {}
        self.capacity = capacity
        self.linked_list = DoublyLinkedList()

    def get(self, key):
        if key in self.sequence:
            node = self.sequence[key]
            self.linked_list.remove(node)
            self.linked_list.insert_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.sequence:
            node = self.sequence[key]
            node.value = value
            self.linked_list.remove(node)
            self.linked_list.insert_head(node)
        else:
            node = Node(key, value)
            self.linked_list.insert_head(node)
            self.sequence[key] = node
            if len(self.sequence) > self.capacity:
                last = self.linked_list.remove_tail()
                self.sequence.pop(last.key)


cache = LRUCache(2)
cache.put(1, 'A')
cache.put(2, 'B')

print(cache.get(1))  # Output: 'A'
cache.put(3, 'C')  # Evicts key 2
print(cache.get(1))  # Output: -1 (not found)
