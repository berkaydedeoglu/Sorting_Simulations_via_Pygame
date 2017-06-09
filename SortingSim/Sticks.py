import random
import stick
import pygame


class Sticks(object):
    def __init__(self):
        self._stick_list = []
        self._biggest = 0  # REVIEW: Biggest niteliği burada mı gerekli yoksa alt sınıfında mı?

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
        new_stick = stick.Stick(random.randint(1, 500), self.nos)  # IDEA:  nos id olarak kullanılabilir mi?

        self.sticks.append(new_stick)

        # color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        color = (15, 156, 15)
        new_stick.color = color

        if new_stick.length > self._biggest:
            self._biggest = new_stick.length

    def new_sticks(self, stick_number: int) -> None:
        i = 0

        while i < stick_number:
            self.new_stick()
            i += 1

    def find_stick(self, length: int, start: int) -> stick:
        """
        for stick_i in self.sticks:
            if stick_i.length == length:
                return stick_i

        """

        if start > len(self.sticks):  # TODO : Hata döndürülmeli
            print("Hata")
            return -1

        i = start

        while i < len(self.sticks):
            if self.sticks[i].length == length:
                return self.sticks[i]
            i += 1

        print("Bulamadı")
        return -1  # self.sticks[start]

    @staticmethod
    def swap_stick_locations(stick_1: stick, stick_2: stick) -> None:
        """
        This is a static method which swaps stick locations.

        We need this method because we need the control on sorting, when
        we show the sorting steps on screen.
        """

        """
        temp_location = stick_1.location
        stick_1.location = stick_2.location
        stick_2.location = temp_location
        # Classic swap algorithm
        """
        temp_location = stick_1.length  # REVIEW : Location değiştirerek hesaplamayı dene. Bunun olması şaşırtıcı
        stick_1.length = stick_2.length
        stick_2.length = temp_location
        # Classic swap algorithm



class SticksToGui(Sticks):  # IDEA: İşler için statik metod mu yoksa iş nesnesi mi daha uygundur?
    """
    This is a working class, that draws sticks to windows (game board) which you give to
    itself as a parameter.

    This class firstly formats the pixels in window then draws sticks according to their
    lengths.
    """

    def __init__(self, board: pygame.display, win_sizes: tuple) -> None:
        super().__init__()
        self.game_board = board
        self.window_sizes = win_sizes

        # scales = self.generate_scale
        # self.draw_sticks(self.sticks_object, self.game_board, scales)

    def generate_scale(self) -> (int, int):
        """
        This function calculates scales. It means how many pixels you need for a stick unit.
        """

        height = self.window_sizes[1]
        length = self.window_sizes[0]

        vertical_scale = (length / self.nos)
        horizontal_scale = int(height / self.biggest)

        scales = (vertical_scale, horizontal_scale)

        return scales

    def draw_sticks(self, scales: (int, int)) -> bool:
        """
        This method draws sticks to pygame board which you give as parameter.
        A stick object has two property:
            - Length (Property)
            - Location

        This method draws sticks according to their location values.
        """

        win_height = self.window_sizes[1]

        for s in self.sticks:
            len_y = s.length * scales[1]
            len_x = scales[0]
            pos_y = win_height - len_y
            pos_x = scales[0] * s.location
            pygame.draw.rect(self.game_board, s.color, (pos_x, pos_y, len_x, len_y))

        return True


if __name__ == "__main__":
    pass
