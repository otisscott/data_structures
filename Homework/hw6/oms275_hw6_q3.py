from DoublyLinkedList import *


class CompactString:
    def __init__(self, orig_str):
        self.string = DoublyLinkedList()
        counter = 1
        letter = orig_str[0]
        for i in range(1, len(orig_str)):
            if orig_str[i-1] == orig_str[i]:
                if i == len(orig_str) - 1:
                    counter += 1
                    self.string.add_last((letter, counter))
                else:
                    counter += 1
            else:
                self.string.add_last((letter, counter))
                counter = 1
                letter = orig_str[i]
                if i == len(orig_str) - 1:
                    self.string.add_last((letter, counter))

    def __add__(self, other):
        return_str = ''
        current = self.string.header.next
        while current != self.string.trailer:
            return_str += current.data[0] * current.data[1]
            current = current.next
        current = other.string.header.next
        while current != other.string.trailer:
            return_str += current.data[0] * current.data[1]
            current = current.next
        return CompactString(return_str)

    def __lt__(self, other):
        min_len = min(len(self.__repr__()), len(other.__repr__()))
        for i in range(min_len):
            if self.__repr__()[i] != other.__repr__()[i]:
                if self.__repr__()[i] >= other.__repr__()[i]:
                    return False
                else:
                    return True
        return True

    def __le__(self, other):
        for i in range(min(len(self.__repr__()), len(other.__repr__()))):
            if self.__repr__()[i] != other.__repr__()[i]:
                if self.__repr__()[i] > other.__repr__()[i]:
                    return False
                else:
                    return True
        return True

    def __gt__(self, other):
        for i in range(min(len(self.__repr__()), len(other.__repr__()))):
            if self.__repr__()[i] != other.__repr__()[i]:
                if self.__repr__()[i] <= other.__repr__()[i]:
                    return False
                else:
                    return True
        return True

    def __ge__(self, other):
        for i in range(min(len(self.__repr__()), len(other.__repr__()))):
            if self.__repr__()[i] != other.__repr__()[i]:
                if self.__repr__()[i] < other.__repr__()[i]:
                    return False
                else:
                    return True
        return True

    def __repr__(self):
        return_str = ''
        current = self.string.header.next
        while current != self.string.trailer:
            return_str += current.data[0] * current.data[1]
            current = current.next
        return return_str
