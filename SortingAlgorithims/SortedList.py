class SortedList:
    """
    This is a list object which is sorted. Actually
    this is not sorted now. Because this is a parent
    class.
    """

    _list = list()

    def __init__(self, arg: list or tuple) -> None:
        try:
            if type(arg) == list:
                self._list = arg
            elif type(arg) == tuple:
                self._list = self.tuple_to_list(arg)
        except:
            raise TypeError("It is not a list or tuple.")

        self.sort()


    @staticmethod
    def tuple_to_list(argtuple: tuple) -> list:
        return [i for i in argtuple]

    def __str__(self) -> str:
        return str(self._list)

    def sort(self) -> None:
        if not (self.__class__.__name__) == "SortedList":
            raise NotImplementedError("Please implement this method.")
        else:
            pass


if __name__ == "__main__":
    obj = SortedList((2, 3, 4))
    print(obj)
