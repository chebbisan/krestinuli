import pygame as pg
import numpy as np

def checkhoriz(map, i, horiz):
    while i < 40 and horiz < 5:
        if map[i][0] == 1 and (map[i][0] != 2 or map[i][0] != 0):
            horiz += 1
        else:
            horiz = 0
        i += 1
    if horiz == 5:
        return True
    return False



pg.init()

dis = pg.display.set_mode((800, 800))

white = (255, 255, 255)
red = (225, 0, 50)
green = (0, 225, 0)
blue = (0, 0, 225)
black = (0, 0, 0)

dis.fill(white)


map = np.zeros((40, 40))

#def check_victory():
#    if 1 in map:
#        if 1 in map[np.where(map == 1)[0]][np.where(map == 1)[1]]:
        



gameover = False


counter = 0

for x in range(0, 800, 20):
    pg.draw.line(dis, black, [x, 0], [x, 800])
    for y in range(0, 800, 20):
        pg.draw.line(dis, black, [800, y], [0, y])

while not gameover:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            gameover=True
        i = 0
        horiz = 0
        if event.type == pg.MOUSEBUTTONDOWN and counter == 0:
            if event.button == 1 and map[event.pos[0]//20][event.pos[1]//20] != 1 and map[event.pos[0]//20][event.pos[1]//20] != 2:
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20 + 20], 3)
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20 + 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20], 3)
                map[event.pos[0]//20][event.pos[1]//20] = 1
                
                pg.display.update()
                counter = 1
                print(checkhoriz(map, i, horiz))
            
        elif event.type == pg.MOUSEBUTTONDOWN and counter == 1:
            if event.button == 1 and map[event.pos[0]//20][event.pos[1]//20] != 1 and map[event.pos[0]//20][event.pos[1]//20] != 2:
                pg.draw.circle(dis, blue, (event.pos[0] - event.pos[0] % 20 + 10,
                 event.pos[1] - event.pos[1] % 20 + 10), 10, 2)
                map[event.pos[0]//20][event.pos[1]//20] = 2
                
                pg.display.update() 
                counter = 0   
        
                    
        
        

    
        

    pg.display.update()
