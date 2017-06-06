from SortingSim import stick
from SortingSim import Sticks

ex1 = Sticks.Sticks(20)
for i in range(10):
    ex1.new_stick()
    print(ex1.sticks[i].length)