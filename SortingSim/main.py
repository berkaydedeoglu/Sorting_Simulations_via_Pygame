import pygame as pg
from SortingSim import Sticks, SortSticks
import time
from threading import Thread

pg.init()
clock = pg.time.Clock()

board = pg.display.set_mode([900, 550], pg.HWSURFACE | pg.SWSURFACE)

sticks = Sticks.SticksToGui(board, (900, 550))
sticks.new_sticks(100)
scales = sticks.generate_scale()
sorted_sticks = SortSticks.SortSticks(sticks)
game_exit = 0
start = time.time()
sort = Thread(target = sorted_sticks.selection_sort)
sort.start()

while not game_exit:
    stop = time.time()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game_exit = 1

    board.fill((30, 32, 35))
    sticks.draw_sticks(scales)
    pg.display.update()
    clock.tick(24)

pg.quit()
quit()
