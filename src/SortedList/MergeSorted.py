from SortedList import SortedList


class MergeSorted(SortedList):
    def __init__(self, arg):
        super().__init__(arg)
        self.devide()

    def sort(self):
        pass

    def merge(self):
        pass

    def devide(self):
        """
        This function seperate the _list step by step. For example:
        _list = [2, 45, 8, 34, 65, 1, 7]
        
        Step 1: [[2, 45, 8, 34]  [65, 1, 7]]
        Step 2: [[ [2, 45], [8, 34] ],[[65, 1], [7] ]]
        Step 3: [[[[2], [45]],[[8],[34]]], [[[65], [1]],[[7]] ]]
         
        Returns Step3 for this example.
        """

        limit = int(len(self._list)/2)
        foo = 0
        mainlist = [self._list]

        while foo < limit:

            for i in mainlist:
                brk = round(len(i) / 2)
                right = i[0:brk]
                left = i[brk:len(i)]
                i = [right, left]
                print(i, end=" | ")
                mainlist = i





            print()
            foo +=1











if __name__ == "__main__":
    """
    obj = MergeSorted([2, 1, -2, 3, 1, 1, 4, 78, -25, 15, 0, 100, 124, 14, 8, 1, 2, 5, 15, 14, 33, 27, 35, 10, 24,
                           32, 57, 51, 90, 1501, 12, 17, 151, 3, 44, 16, 16, -87, 65, 84, 45])
    """
    obj = MergeSorted((2, 45, 8, 34, 65, 1, 7, 2, 5))
    print(obj)

