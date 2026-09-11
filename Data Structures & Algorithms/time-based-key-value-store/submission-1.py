from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.map[key]

        l = -1
        r = len(val_list)
        while l + 1 < r:
            mid = (l + r) // 2
            if val_list[mid][1] <= timestamp:
                l = mid
            else:
                r = mid
        return val_list[l][0] if l != -1 else ""
