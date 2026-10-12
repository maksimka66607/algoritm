"""Динамический массив с удвоением вместимости."""
import ctypes


class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 1
        self._data = (ctypes.py_object * self._capacity)()

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index < self._size:
            raise IndexError(index)
        return self._data[index]

    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError(index)
        self._data[index] = value

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def append(self, value):
        if self._size == self._capacity:
            self._capacity *= 2
            data = (ctypes.py_object * self._capacity)()
            for i in range(self._size):
                data[i] = self._data[i]
            self._data = data
        self._data[self._size] = value
        self._size += 1

    def pop(self):
        if not self._size:
            raise IndexError('empty array')
        self._size -= 1
        value = self._data[self._size]
        self._data[self._size] = None
        return value
