class vector:
    def __init__(self, data):
        self.data = list(data)

    def __str__(self):
        return ":".join(map(str, self.data))

    def __add__(self, other):
        if isinstance(other, vector):
            other = other.data
        return vector([x + y for x, y in zip(self.data, other)])

    def __radd__(self, other):
        return self + other

    def __matmul__(self, other):
        if isinstance(other, vector):
            other = other.data
        return sum(x * y for x, y in zip(self.data, other))
