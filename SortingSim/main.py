import pygame as pg
from SortingSim import Sticks



sticks = Sticks.Sticks()
sticks.new_sticks(100)

#ex2 = SortSticks.SortSticks(sticks)
#ex2.sort()

pg.init()
clock = pg.time.Clock()

board = pg.display.set_mode([900, 550], pg.HWSURFACE | pg.SWSURFACE)
Gsticks = Sticks.SticksToGui(sticks, board, (900, 550))
scales = Gsticks.generate_scale()
game_exit = 0

while not game_exit:

    for e in pg.event.get():
        if e.type == pg.QUIT:
            game_exit = 1

    board.fill((30, 32, 35))
    Gsticks.draw_sticks(scales)
    pg.display.update()
    clock.tick(14)


pg.quit()
quit()
