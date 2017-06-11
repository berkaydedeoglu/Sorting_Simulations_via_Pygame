import pygame as pg
import Sticks, SortSticks, SettingWindow
import time
from threading import Thread

setting_window = SettingWindow.SettingWindow()
settings = setting_window.settings
pg.init()
clock = pg.time.Clock()

board = pg.display.set_mode([900, 550], pg.HWSURFACE | pg.SWSURFACE)

font = pg.font.Font(None, 18)
status = font.render("Algorithm: Selection Sort, Time: , Speed: ", False, (156, 20, 180))
sticks = Sticks.SticksToGui(board, (900, 550))
sticks.new_sticks(settings[0], settings[3])

scales = sticks.generate_scale()
sorted_sticks = SortSticks.SortSticks(sticks)
sorted_sticks.speed = settings[2]

game_exit = 0

start = time.time()

sort = Thread(target=sorted_sticks.sort, args=(settings[1],))
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
    clock.tick(60)

pg.quit()
exit()
