from SortedList import SortedList


class SelectionSorted(SortedList):

    def __init__(self, arg: list or tuple) -> None:
        super().__init__(arg)

    def sort(self): # Todo: Check steps via print()
        i = 0
        length = len(self._list)

        while i < length:
            s_index = self.smallest(i, length)
            temp = self._list[i]

            self._list[i] = self._list[s_index]
            self._list[s_index] = temp

            i += 1

    def smallest(self, step, stop):
        foo = step
        temp = self._list[foo]
        index = foo
        while foo < stop:
            if self._list[foo] < temp:
                temp = self._list[foo]
                index = foo
            foo += 1

        return index


if __name__ == "__main__":
    obj = SelectionSorted([2, 1, -2, 3, 1, 1, 4, 78, -25, 15, 0, 100, 124, 14, 8, 1, 2, 5, 15, 14, 33, 27, 35, 10, 24,
                           32, 57, 51, 90, 1501, 12, 17, 151, 3, 44, 16, 16, -87, 65, 84, 45])
    print(obj)
