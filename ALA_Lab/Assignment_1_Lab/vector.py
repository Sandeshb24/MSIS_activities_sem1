import math


class Vector:
    """Vector with tuple storage."""

    def __init__(self, entries):
        self.entries = tuple(float(x) for x in entries)

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, i):
        return self.entries[i]

    def __iter__(self):
        return iter(self.entries)

    def __repr__(self):
        return f"Vector({self.entries})"

    def add(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension mismatch")
        return Vector(a + b for a, b in zip(self, other))

    def scale(self, c):
        return Vector(c * a for a in self)

    def dot(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension mismatch")
        return sum(a * b for a, b in zip(self, other))

    def norm(self):
        return math.sqrt(self.dot(self))

    def cosine_similarity(self, other):
        n1, n2 = self.norm(), other.norm()
        if n1 == 0 or n2 == 0:
            raise ValueError("Cosine similarity undefined for zero vector")
        return self.dot(other) / (n1 * n2)

    # ---- Assignment 2 additions ----
    def mean(self):
        if len(self) == 0:
            raise ValueError("Mean of empty vector")
        return sum(self.entries) / len(self)

    def demean(self):
        m = self.mean()
        return Vector(a - m for a in self)

    def std(self):
        d = self.demean()
        return math.sqrt(d.dot(d) / len(self))
