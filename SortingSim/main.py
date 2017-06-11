import pygame as pg
import Sticks, SortSticks
import time
from threading import Thread

pg.init()
clock = pg.time.Clock()

board = pg.display.set_mode([900, 550], pg.HWSURFACE | pg.SWSURFACE)

font = pg.font.Font(None, 18)
status = font.render("Algorithm: Selection Sort, Time: , Speed: ", False ,(156, 20, 180))
sticks = Sticks.SticksToGui(board, (900, 550))
sticks.new_sticks(100)

scales = sticks.generate_scale()
sorted_sticks = SortSticks.SortSticks(sticks)

game_exit = 0

start = time.time()

sort = Thread(target=sorted_sticks.sort, args=("selection_sort",))
sort.start()


while not game_exit:
    if sort.is_alive():
        stop = time.time()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game_exit = 1
        if e.type == pg.key:
            print(e)

    board.fill((30, 32, 35))
    status = font.render("Algorithm: Selection Sort,      Time: %f,     Swap Time: %d " %((stop-start), sorted_sticks.swap_time), False, (156, 20, 180))
    board.blit(status, (0, 0))
    sticks.draw_sticks(scales)
    pg.display.update()
    clock.tick(24)

pg.quit()
quit()
