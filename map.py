
class Map:
    def __init__(self):
        self._entry_list = list()

    def __len__(self):
        return len(self._entry_list)

    def __contains__(self, key):
        index = self.findKey(key)
        return index is not None

    def add(self, key, value):
        index = self.findKey(key)
        if index is None:
            self._entry_list.append(MapEntry(key, value))
            return True
        else:
            self._entry_list[index].value = value
            return False

    def remove(self, key):
        index = self.findKey(key)
        assert index is not None, "Invalid map key."
        self._entry_list.pop(index)

    def __iter__(self):
        return MapIterator(self._entry_list)

    def findKey(self, key):
        return self._entry_list.index(key)


class MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MapIterator:
    def __init__(self, list):
        self._list_reference = list
        self._current_index = 0

    def __iter__(self):
           return self

    def __next__(self):
        if self._current_index < len(self._list_reference):
            element = self._list_reference[self._current_index]
            self._current_index += 1
            return element
        else:
            raise StopIteration