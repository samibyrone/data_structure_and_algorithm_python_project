class Map:

    def __init__(self):
        self.map = {}

    def isEmpty(self):
        return not bool(self.map)

    def size(self):
        return len(self.map)

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, None)

    def replace(self, key, value):
        if key in self.map:
            self.map[key] = value

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def hashCode(self):
        return hash(frozenset(self.map.values()))

    def compute(self, key, func):
        self.map[key] = func(self.map.get(key, None))

    def compute_if_present(self, key, func):
        if key in self.map:
            self.map[key] = func(self.map[key])

    def compute_if_absent(self, key, func):
        if key in self.map:
            self.map[key] = func()

    def contains_key(self, key):
        return key in self.map

    def contains_value(self, value):
        return value in self.map
