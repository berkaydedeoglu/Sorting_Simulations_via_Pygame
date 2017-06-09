import Sticks
# from SortingSim import stick
import time


class SortSticks(object):
    def __init__(self, sticks_object: Sticks):

        self.sticks = sticks_object
        self._length_list = [stick.length for stick in self.sticks.sticks]

    @property
    def length_list(self) -> list:
        return self._length_list

    def swap(self, index_1: int, index_2: int, in_from: int) -> None:  # FIXME: in_from parametresini işlevli olarak kullandığımda hata alıyorum.

        # Swapping stick locations!!
        stick_1 = self.sticks.find_stick(self.length_list[index_1], in_from)
        stick_2 = self.sticks.find_stick(self.length_list[index_2], in_from)
        self.sticks_on((stick_1, stick_2))
        time.sleep(0.08)
        self.sticks.swap_stick_locations(stick_1, stick_2)
        self.sticks_off((stick_1, stick_2))

        # Swapping list items
        temp = self.length_list[index_1]
        self.length_list[index_1] = self.length_list[index_2]
        self.length_list[index_2] = temp

    @staticmethod
    def sticks_on(stick: tuple) -> None:
        stick[0].color = (255, 0, 255)  # TODO: Renkleri düzelt
        stick[1].color = (255, 255, 255)

    @staticmethod
    def sticks_off(stick: tuple) -> None:
        stick[0].color = (15, 156, 15)
        stick[1].color = (15, 156, 15)

    def test_sort(self):
        i = 0
        while i < len(self.length_list)-1:
            self.swap(i, i+1, 0)
            i += 1

    def selection_sort(self):
        len_list = len(self.length_list)

        def smallest(step: int) -> int:
            temp = self.length_list[step]
            i = step
            index = i

            while i < len_list:
                if self.length_list[i] < temp:
                    temp = self.length_list[i]
                    index = i
                i += 1

            return index

        def sort():
            i = 0
            while i < len_list:
                small = smallest(i)
                self.swap(i, small, i)
                i += 1

        sort()

if __name__ == "__main__":
    sticks = Sticks.Sticks()
    sticks.new_sticks(10)
    ex = SortSticks(sticks)
    print(ex.length_list)
