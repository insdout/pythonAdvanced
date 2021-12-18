class Queue:
    def __init__(self):
        self.push_buffer = []
        self.pop_buffer = []

    def push(self, x):
        self.push_buffer.append(x)

    def pop(self):
        if len(self.pop_buffer) == 0:
            if len(self.push_buffer) > 0:
                while len(self.push_buffer) > 0:
                    self.pop_buffer.append(self.push_buffer.pop())
                return self.pop_buffer.pop()
            else:
                raise IndexError('pop from an empty queue')
        else:
            return self.pop_buffer.pop()
