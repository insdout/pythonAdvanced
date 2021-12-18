class Buffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.storage = []

    def add(self, *a):
        self.storage.extend(a)
        while len(self.storage) >= self.maxsize:
            print(sum(self.storage[:self.maxsize]))
            self.storage = self.storage[self.maxsize:]

    def get_current_part(self):
        return self.storage
