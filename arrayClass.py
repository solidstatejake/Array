# Implements an array ADT using array capabilities of ctypes module; a module which allows
# for use of data structures from the C language and relevant libraries.
import ctypes


class Array:

    def __init__(self, size):
        assert size > 0, "Array size must be greater than 0."
        self.size = size
        PyArrayType = ctypes.py_object * size
        self.elements = PyArrayType()
        self.clear(0)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array subcript out of range."
        return self.elements[index]

    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array subcript out of range."
        self.elements[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self.elements)


class _ArrayIterator:

    def __init__(self, array):
        self._array_reference = array
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self._array_reference):
            element = self._array_reference[self._current_index]
            self._current_index += 1
            return element
        else:
            raise StopIteration


class Array2D:

    def __init__(self, nrow, ncol):
        assert nrow > 0 and ncol > 0, "Number of rows and columns must be greater than 0."
        self.nrow = nrow
        self.ncol = ncol
        self._row_array = Array(nrow)

        for i in range(nrow):
            self._row_array[i] = Array(ncol)

        for row in self._row_array:
            row.clear(None)

    def __getitem__(self, index_tuple):
        assert len(index_tuple) == 2, "Must provide exactly two indices."

        row = index_tuple[0]
        col = index_tuple[1]

        assert 0 <= row < self.nrow \
               and 0 <= col < self.ncol, "Array subscript out of bounds."

        _1d_array = self._row_array[row]
        return _1d_array[col]

    def __setitem__(self, index_tuple, value):
        assert len(index_tuple) == 2, "Must provide exactly two indices."

        row = index_tuple[0]
        col = index_tuple[1]

        assert 0 <= row < self.nrow \
            and 0 <= col < self.ncol, "Array subscript out of bounds."

        _1d_array = self._row_array[row]
        _1d_array[col] = value

    def clear(self, value):
        for row in self._row_array:
            row.clear(value)
