class FlashError(Exception):
    pass


class FlashMaxFileSizeError(FlashError):
    pass


class FlashMemoryLimitError(FlashError):
    pass


class Flash:
    def __init__(self, capacity, max_file_size=None):
        self.capacity = capacity
        self.max_file_size = max_file_size

    def write(self, v):
        if self.max_file_size is not None:
            if v > self.max_file_size:
                raise FlashMaxFileSizeError

        if v > self.capacity:
            raise FlashMemoryLimitError
        else:
            self.capacity -= v
