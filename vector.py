import math

class Vector:

    def __init__(self, element_list = []):
        self._validate(element_list)
        self._elements = element_list
        self._length = len(element_list)
        self._squares = list(element ** 2 for element in self._elements)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        assert isinstance(index, int), "Must index with int."
        return self._elements[index]

    def __setitem__(self, index, value):
        assert isinstance(index, int) and isinstance(value, (int, float)), "Must index with int to set int or float."
        self._elements[index] = value

    def __add__(self, vector):
        assert isinstance(vector, Vector) and len(self) == len(vector), "Must add vectors of equal size."
        elements = list(self[i] + vector[i] for i in range(len(self)))
        return Vector(elements)

    def __sub__(self, vector):
        assert isinstance(vector, Vector) and len(self) == len(vector), "Must subtract vectors of equal size."
        return Vector(list(self[i] - vector[i] for i in range(len(self))))

    def __mul__(self, scalar):
        assert isinstance(scalar, (int, float)), "Multiplication of vector must be with scalar."
        return Vector(list(element * scalar for element in self._elements))

    def __pow__(self, power):
        elements = list(element ** power for element in self._elements)
        return Vector(elements)

    def __eq__(self, vector):
        assert isinstance(vector, Vector), "Must compare vectors."
        if len(self) != len(vector):
            return False
        for i in range(len(self)):
            if self[i] != vector[i]:
                return False
        return True

    def __ne__(self, vector):
        assert isinstance(vector, Vector), "Must compare vectors."
        if len(self) != len(vector):
            return True
        for i in range(len(self)):
            if self[i] != vector[i]:
                return True
        return False

    def __str__(self):
        string = "<"
        for element in self:
            if element == self[-1]:
                string += str(element)
            else:
                string += str(element) + ", "
        string += ">"
        return string

    def magnitude(self):
        return sum(self._squares) ** 0.5

    # Return self as unit vector
    def unit(self):
        return Vector(list(element / sum(self._squares) for element in self._elements))

    def dot(self, vector):
        assert isinstance(vector, Vector) and len(vector) == len(self),  "Dot product must involve vectors " \
                                                                         "of equal length as operands."
        return sum(list(self[i] * vector[i] for i in range(len(self))))

    # def angle(self):
    #     return math.acos(self.dot(self) / (self.magnitude ** 2))

    def _validate(self, element_list):
        for element in element_list:
            assert isinstance(element, (int, float)), "Elements of vector must be integers or floating-point numbers."


x = Vector([1,2,3])
y = Vector([2,4,9])

z = x-y
print(str(x) + " - " + str(y) + " = " + str(z))
print(x.dot(y))
