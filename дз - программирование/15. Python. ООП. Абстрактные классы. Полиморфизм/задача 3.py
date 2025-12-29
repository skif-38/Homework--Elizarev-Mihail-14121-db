class Counter:
    def __init__(self, start=0):
        self.value = max(0, start)
    
    def inc(self, n=1):
        self.value += n
    
    def dec(self, n=1):
        self.value = max(0, self.value - n)


class NonDecCounter(Counter):
    def dec(self, n=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        super().__init__(start)
        self.limit = limit
    
    def inc(self, n=1):
        self.value = min(self.value + n, self.limit)