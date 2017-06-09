from SortingSim import Sticks
from SortingSim import stick
import time

"""
    # ///---=== FIND  STICK TEST ===---

ex1 = Sticks.Sticks()
ex1.new_sticks(10)
a = [i.length for i in ex1.sticks]
print(a)
print([ex1.find_stick(i, 0).location for i in a])
print([ex1.find_stick(i, 0).location for i in a])

    # ///---=== FIND  STICK TEST ===---
"""

"""
    # ///---=== SWAP STICK TEST ===---

s1 = stick.Stick(20, 130)
s2 = stick.Stick(13, 1)
s3 = stick.Stick(103, 58)

print("s1 nesnesinin id'si: %d konumu: %d" % (s1.o_id, s1.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s2.o_id, s2.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s3.o_id, s3.location))

Sticks.Sticks().swap_stick_locations(s1, s2)
print("\nKonumlar değiştirildi (s1, s2)!!\n")

print("s1 nesnesinin id'si: %d konumu: %d" % (s1.o_id, s1.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s2.o_id, s2.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s3.o_id, s3.location))

Sticks.Sticks().swap_stick_locations(s1, s3)
print("\nKonumlar değiştirildi (s1, s3)!!\n")

print("s1 nesnesinin id'si: %d konumu: %d" % (s1.o_id, s1.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s2.o_id, s2.location))
print("s2 nesnesinin id'si: %d konumu: %d" % (s3.o_id, s3.location))

    # ///---=== SWAP STICK TEST ===---
"""