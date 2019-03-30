from SortedList import SortedList


class BubbleSorted(SortedList):

    def __init__(self, arg):
        super().__init__(self, arg)

    def sort(self) -> None:

        li = self._list
        i = len(li)

        while i > 1:
            j = 0
            while j < i-1:
                if li[j] > li[j+1]:
                    self.swap(li, j, j+1)
                j += 1
            i -= 1

    @staticmethod
    def swap(li: list, index_1: int, index_2: int) -> None:

        temp = li[index_1]
        li[index_1] = li[index_2]
        li[index_2] = temp


if __name__ == "__main__":
    obj = BubbleSorted([2, 1, -2, 3, 1, 1, 4, 78, -25, 15, 0, 100, 124, 14, 8, 1, 2, 5, 15, 14, 33, 27, 35, 10, 24,
                        32, 57, 51, 90, 1501, 12, 17, 151, 3, 44, 16, 16, -87, 65, 84, 45])
    print(obj)
