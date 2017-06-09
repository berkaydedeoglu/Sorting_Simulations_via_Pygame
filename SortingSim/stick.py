class Stick:
    def __init__(self, length=None, location=None):

        self._length = length

        self._loc = location

        self._id = id(self)

        self._color = None

        # fixme: Verilere setter metodu ile yükleme yapılması!

    @property
    def length(self):
        return self._length

    @property
    def location(self):
        return self._loc

    @property
    def o_id(self):
        return self._id

    @property
    def color(self):
        return self._color

    @length.setter
    def length(self, value):
        self._length = value

    @location.setter
    def location(self, location):
        self._loc = location

    @color.setter
    def color(self, value: tuple):
        if value[0] <= 255 and value[1] <= 255 and value[2] <= 255 \
                and value[0] >= 0 and value[1] >= 0 and value[2] >= 0:

            self._color = value
        else:
            self._color = (255, 255, 255)


if __name__ == "__main__":
    stick = Stick()
    stick.length(120)
    stick.location(0)

    print(stick.length, stick.location)
