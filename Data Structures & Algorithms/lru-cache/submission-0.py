class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.start = TreeNode(0,0)
        self.end = TreeNode(0,0)
        self.start.next = self.end
        self.end.prev = self.start   

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next = self.start.next
        self.start.next = node
        node.next.prev = node
        node.prev = self.start

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.map) < self.capacity:
                self.map[key] = TreeNode(key, value)
                self.insert(self.map[key])
            else:
                lru_node = self.end.prev
                lru_key = lru_node.key
                self.remove(lru_node)
                del self.map[lru_key]
                self.map[key] = TreeNode(key, value)
                self.insert(self.map[key])
