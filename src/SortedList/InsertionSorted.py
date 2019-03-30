from SortedList import SortedList


class InsertionSorted(SortedList):
    def sort(self):

        li = self._list
        length = len(li)
        i = 0

        while i < (length - 1):
            if li[i] > li[i + 1]:
                self.swap_and_check(i)
            i += 1

    def swap_and_check(self, index: int) -> None:

        li = self._list
        i = index + 1  # Firstly they have to be changed!

        while i > 0:
            if li[i] < li[i - 1]:
                temp = li[i]
                li[i] = li[i - 1]
                li[i - 1] = temp

            i -= 1


if __name__ == "__main__":
    obj = InsertionSorted([2, 1, -2, 3, 1, 1, 4, 78, -25, 15, 0, 100, 124, 14, 8, 1, 2, 5, 15, 14, 33, 27, 35, 10, 24,
                           32, 57, 51, 90, 1501, 12, 17, 151, 3, 44, 16, 16, -87, 65, 84, 45])
    print(obj)
