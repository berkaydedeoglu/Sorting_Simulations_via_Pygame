import pygame as pg
from SortingSim import Sticks

sticks = Sticks.Sticks()
sticks.new_sticks(50)
pg.init()
clock = pg.time.Clock()

board = pg.display.set_mode([700, 550], pg.HWSURFACE | pg.SWSURFACE)
Gsticks = Sticks.SticksToGui(sticks, board, (700, 550))
scales = Gsticks.generate_scale()
game_exit = 0
while not game_exit:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit_game = 1

    board.fill((32, 32, 32))
    Gsticks.draw_sticks(scales)
    pg.display.update()
    clock.tick(25)


pg.quit()
quit()
