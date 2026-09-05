class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.l = []
        self.n = 0

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = self.n
        self.l.append(val)
        self.n += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        last_index = self.n - 1
        last_value = self.l[last_index]
        self.l[last_index] = val
        self.l[index] = last_value
        self.map[last_value] = index
        del self.map[val]
        self.l.pop()

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()