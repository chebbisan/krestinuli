import pygame as pg

pg.init()

dis = pg.display.set_mode((800, 800))

white = (255, 255, 255)
red = (225, 0, 50)
green = (0, 225, 0)
blue = (0, 0, 225)
black = (0, 0, 0)

dis.fill(white)

gamemap = []

for p in range(40):
    gamemap.append((0, 0))
print(gamemap)

gameover = False

counter = 0

while not gameover:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            gameover=True
        if event.type == pg.MOUSEBUTTONDOWN and counter == 0:
            if event.button == 1:
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20 + 20], 3)
                pg.draw.line(
                    dis, red, [event.pos[0] - event.pos[0] % 20, event.pos[1] - event.pos[1] % 20 + 20],
                     [event.pos[0] - event.pos[0] % 20 + 20, event.pos[1] - event.pos[1] % 20], 3)
                pg.display.update()
                counter = 1
            
        elif event.type == pg.MOUSEBUTTONDOWN and counter == 1:
            if event.button == 1:
                pg.draw.circle(dis, blue, (event.pos[0] - event.pos[0] % 20 + 10,
                 event.pos[1] - event.pos[1] % 20 + 10), 10, 2)
                pg.display.update() 
                counter = 0   
                    

        

    
        for x in range(0, 800, 20):
            pg.draw.line(dis, black, [x, 0], [x, 800])
        for y in range(0, 800, 20):
            pg.draw.line(dis, black, [800, y], [0, y])

    pg.display.update()
