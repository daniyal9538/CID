import time
import pygame
import sys
from helper import *





l1 = 0
l2 = 426
m1 = 426
m2 = 426+426
r1 = 426+426
r2 = 1280
m = [m1, m2]
r = [r1, r2]
l = [l1, l2]
loc = [l, m, r]

data=dict()
data = helper.getFrameData('city_data_100.json')
#data = helper.delPoly(data)
data = helper.getXLocA(data)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
for count, i in enumerate(data):
  screen.fill((0,0,0))
  #x=x+x
  #y=y+y
  color = (255, 100, 0)
  #pygame.draw.rect(screen, color, pygame.Rect(x, x, y, y))
  #message_display('Test', l1, l2)
  text= []
  for det in i['objects']:
    t1=dict()
    t1['text'] = det['name']
    #t1['XLoc'] = loc[det['x_loc']]
    t1['XLoc'] = det['x_loc']
    #print(t1['XLoc'], det['midX'])
    text.append(t1)
  
  min , max = laneBoundary(i['lanePts'], i['lanePolygon'])
  print(int((min/480)*1280),int(((max-min)/480)*1280), min, max-min, count)
  pygame.draw.rect(screen, (0,200,0), [int((min/480)*1280), 0, int(((max-min)/480)*1280), 720], 12)
  display_with_linesA(text, screen)
  
  pygame.display.update()
  #print(i)
  time.sleep(1)
  
  pressed = pygame.key.get_pressed()
  for event in pygame.event.get():
        if event.type == pygame.QUIT: 
          sys.exit(0)
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            sys.exit(0)
