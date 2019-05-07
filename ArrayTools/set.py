

class Set:

    def __init__(self, element_list):
        self.elements = list(filter(lambda e: e not in self.elements, element_list))

    def __len__(self):
        return len(self.elements)

    def __contains__(self, element):
        return element in self.elements

    def contains(self, element):
        return element in self.elements

    def add(self, element):
        if element not in self:
            self.elements.append(element)

    def remove(self, element):
        assert element in self, "Element to be removed must be in set."
        self.elements.remove(element)

    def __eq__(self, other_set):
        if len(self) != len(other_set):
            return False
        else:
            return self.isSubsetOf(other_set)

    def isSubsetOf(self, other_set):
        if len(self) > len(other_set):
            return False
        for element in self.elements:
            if element not in other_set.elements:
                return False
        return True

    def isProperSubsetOf(self, other_set):
        if not len(self) < len(other_set):
            return False
        for element in self.elements:
            if element not in other_set.elements:
                return False
        return True

    def union(self, other_set):
        if len(self) > len(other_set):
            new_set = self
            for element in other_set.elements:
                if element not in new_set:
                    new_set.add(element)
        else:
            new_set = other_set
            for element in self.elements:
                if element not in new_set:
                    new_set.add(element)
        return new_set

    def intersection(self, other_set):
        new_set = Set()
        if len(self) > len(other_set):
            for element in other_set:
                if element in self.elements:
                    new_set.add(element)
        else:
            for element in self.elements:
                if element in other_set.elements:
                    new_set.add(element)
        return new_set

    def difference(self, other_set):
        new_set = Set()
        for element in self.elements:
            if element not in other_set.elements:
                new_set.add(element)
        return new_set

    def __lt__(self, other_set):
        return self.isProperSubsetOf(other_set)

    def __le__(self, other_set):
        return self.isSubsetOf(other_set)

    def __gt__(self, other_set):
        return other_set.isProperSubsetOf(self)

    def __ge__(self, other_set):
        return other_set.isSubsetOf(self)

    def __add__(self, other_set):
        return self.union(other_set)

    def __mul__(self, other_set):
        return self.intersection(other_set)

    def __sub__(self, other_set):
        return self.difference(other_set)

    def __iter__(self):
        return _SetIterator(self.elements)


class _SetIterator:

    def __init__(self, set):
        self._set_reference = set
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self._set_reference):
            element = self._set_reference[self._current_index]
            self._current_index += 1
            return element
        else:
            raise StopIteration
