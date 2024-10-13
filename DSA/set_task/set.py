class Set:

    def __init__(self):
        self.set = []

    def isEmpty(self):
        return len(self.set) == 0

    def add(self, element):
        if element not in self.set:
            self.set.append(element)

    def remove(self, element):
        if element in self.set: self.set.remove(element)
        else: print(f"Element {element} not found in set")

    def size(self):
        return len(self.set)

    def contains(self, element):
        return element in self.set

    def clear(self):
        self.set = []

    def intersection(self, elements):
        output = Set()
        for element in elements.set:
            output.add(element)
        return output

    def union(self, elements):
        output = Set()
        output.set = self.set[:]
        for element in elements.set:
            if element not in output.set:
                output.add(element)
        return output

    def difference(self, elements):
        output = Set()
        for element in self.set:
            if element not in elements.set:
                output.add(element)
        return output

