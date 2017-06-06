class Stick:

    def __init__(self, length=None, location=None):

        self._length = length
        self._loc = location

    @property
    def length(self):
        return self._length

    @property
    def location(self):
        return self._loc

    @length.setter
    def length(self, value):
        self._length = value

    @location.setter
    def location(self, location):
        self._loc = location

if __name__ == "__main__":
    stick = Stick()
    stick.length(120)
    stick.location(0)

    print(stick.length, stick.location)


