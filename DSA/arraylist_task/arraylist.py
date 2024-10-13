class ArrayList:

    def __init__(self):
        self.array = []
        self.element = 50
        self.size = 0

    def add(self, content):
        if self.size >= self.element:
            self.resize()
        self.array.append(content)
        self.size += 1

    def resize(self):
        self.element *= 2
        new_array = [None] * self.element
        for index in range(self.size):
            new_array[index] = self.array[index]
            self.array = new_array

    def remove(self, content):
        if content in self.array:
            self.array.remove(content)
            self.size -= 1

    def  get(self, contain):
        if 0 <= contain < self.size:
            return self.array[contain]
        return None

    def is_empty(self):
        return len(self.array) == 0

    def total_size(self):
        return len(self.array)

    def last_index_of(self, content):
        for index in range(self.size -1, -1, -1):
            if self.array[index] == content:
                return index
        return -1

    def list_iterator(self, container = 0):
        if 0 <= container < self.size:
            for index in range(container, self.size):
                yield self.array[index]
        else:raise IndexError('list index out of range')

    def spliterator(self):
        middle = self.size // 2
        return self.array[:middle], self.array[middle:]

    def clone(self):
        new_array = ArrayList()
        new_array.array = self.array[:]
        new_array.size = self.size
        new_array.element = self.element
        return new_array