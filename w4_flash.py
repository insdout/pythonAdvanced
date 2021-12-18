class Flash:
    def __init__(self, capacity):
        self.capacity = capacity

    def write(self, filesize):
        if filesize <= self.capacity:
            self.capacity -= filesize
        else:
            raise ValueError
