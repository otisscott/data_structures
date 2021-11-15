class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        else:
            self.coords = d

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result.coords[j] = self.coords[j] + other.coords[j]
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result.coords[j] = self.coords[j] - other.coords[j]

    def __neg__(self):
        negative = Vector(len(self))
        for i in range(len(self.coords)):
            negative.coords[i] = self.coords[i] * -1
        return negative

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = 0
            if len(self.coords) != len(other.coords):
                raise ValueError("dimensions must agree")
            else:
                for i in range(len(self.coords)):
                    result += self.coords[i] * other.coords[i]
                return result
        else:
            multiplied = Vector(len(self.coords))
            for i in range(len(self.coords)):
                multiplied[i] = self.coords[i] * other
            return multiplied

    def __rmul__(self, other):

        multiplied = Vector(len(self.coords))
        for i in range(len(self.coords)):
            multiplied[i] = self.coords[i] * other
        return multiplied

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "<"+str(self.coords)[1:-1]+">"

    def __repr__(self):
        return str(self)


def main():
    v1 = Vector(5)
    v1[1] = 10
    v1[-1] = 10
    print(v1)
    v2 = Vector([2, 4, 6, 8, 10])
    print(v2)
    u1 = v1 + v2
    print(u1)
    u2 = -v2
    print(u2)
    u3 = 3 * v2
    print(u3)
    u4 = v2 * 3
    print(u4)
    u5 = v1 * v2
    print(u5)
