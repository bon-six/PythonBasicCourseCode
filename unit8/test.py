

from tetris import Tetris
import pygame

import settings
import tetris

import timeit

import time


pygame.init()


well_obj = tetris.WellObject(300,500,settings.color_black)
well_obj.grid[0][4]='-'
well_obj.grid[1][5]='O'
well_obj.grid[4][9]='S'
well_obj.grid[3][8]='L'
well_obj.grid[6][2]='T'
well_obj.grid[9][3]='Z'
well_obj.grid[3][19]='J'

start_time = time.time()
for i in range(10000):
    well_obj.update_well() 
print("--- %s seconds ---" % (time.time() - start_time))

