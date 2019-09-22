import pygame as pg

def get_colors(colors):
    for i in colors:
        for x in range(3):
            i[x]=i[x]*255
    return colors

pg.init()

width = 400 
height = 300

gameDisplay = pg.display.set_mode((width, height))
pg.display.set_caption('demo')

black =[0, 0, 0]
white =[1, 1, 1]

colors =[black, white]

new_colors = get_colors(colors)


#figure out way to algorythmically create 2d sprites in game, numpy masks?

dImg1 = pg.image.load('dObject1.png')

#print(dImg1, 'test', type(dImg1))
#print (new_colors)


clock = pg.time.Clock()

end = False

while not end:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            end = True
    
        print(event)

    pg.display.update()

    clock.tick(60)
pg.quit()
#quit()