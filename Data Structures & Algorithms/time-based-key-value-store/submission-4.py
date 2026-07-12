class TimeMap:
    def __init__(self):
        self.keymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap[key] = []
        self.keymap[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keymap:
            return ""
        
        temp = self.keymap[key]
        if timestamp < temp[0][0]:
            return ""
        hi = len(temp)
        lo = 0 
        mid = (hi + lo) // 2

        while lo < hi:
            mid = (hi + lo) // 2
            if temp[mid][0] > timestamp:
                hi = mid
            else:
                lo = mid + 1
        return temp[lo - 1][1]