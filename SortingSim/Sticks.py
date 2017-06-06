import random
from SortingSim import stick
import pygame


class Sticks(object):
    def __init__(self):
        self._stick_list = []
        self._biggest = 0

    @property
    def biggest(self):
        return self._biggest

    @property
    def sticks(self):
        return self._stick_list

    @property
    def nos(self):
        return len(self.sticks)

    def new_stick(self) -> None:
        new_stick = stick.Stick(random.randint(1, 500), self.nos)
        self.sticks.append(new_stick)

        if new_stick.length > self._biggest:
            self._biggest = new_stick.length

    def new_sticks(self, stick_number):
        i = 0

        while i < stick_number:
            self.new_stick()
            i += 1


class SticksToGui:  # SOR: İşler için statik metod mu yoksa iş nesnesi mi daha uygundur?
    """
    This is a working class, that draws sticks to windows (game board) which you give to
    itself as a parameter.

    This class firstly formats the pixels in window then draws sticks according to their
    lengths.
    """

    def __init__(self, sticks_o: Sticks, board: pygame, win_sizes: (int, int)) -> None:
        self.sticks_object = sticks_o
        self.game_board = board
        self.window_sizes = win_sizes

        scales = self.generate_scale()
        # self.draw_sticks(self.sticks_object, self.game_board, scales)

    def generate_scale(self) -> (int, int):
        """
        This function calculates scales. It means how many pixels you need for a stick unit.
        """

        height = self.window_sizes[1]
        length = self.window_sizes[0]

        vertical_scale = int(length / self.sticks_object.nos)
        horizontal_scale = int(height / self.sticks_object.biggest)

        scales = (vertical_scale, horizontal_scale)

        return scales

    def draw_sticks(self, scales: (int, int)) -> bool:
        win_height = self.window_sizes[1]

        for s in self.sticks_object.sticks:
            len_y = s.length * scales[1]
            len_x = scales[0]
            pos_y = win_height - len_y
            pos_x = scales[0] * s.location
            pygame.draw.rect(self.game_board, (0, 153, 0), (pos_x, pos_y, len_x, len_y))

        return True


if __name__ == "__main__":
    pass
