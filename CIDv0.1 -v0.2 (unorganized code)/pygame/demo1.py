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
data = helper.getFrameData('demo_city_data_100.json')
#data = helper.delPoly(data)
data = helper.getXLocA(data)

green = (0,200, 0)
grey = (200, 200, 200)
yellow = (222,200,0)
blue = (0,0,200)
red = (200, 0, 0)
orange  = (236, 166, 25)


pygame.init()
screen = pygame.display.set_mode((1280, 720))


for count, i in enumerate(data):
  screen.fill((0,0,0))
  min , max = laneBoundary(i['lanePts'], i['lanePolygon'])
  #print(int((min/480)*1280),int(((max-min)/480)*1280), min, max-min, count)
  pygame.draw.rect(screen, grey, [0, 0, 1280, 144], 2)
  pygame.draw.rect(screen, grey, [0, 0, 1280, 288], 2)
  pygame.draw.rect(screen, grey, [0, 0, 1280, 432], 2)
  pygame.draw.rect(screen, grey, [0, 0, 1280, 576], 2)
  pygame.draw.rect(screen, grey, [0, 0, 1280, 720], 2)
  pygame.draw.rect(screen, green, [int((min/480)*1280), 0, int(((max-min)/480)*1280), 720], 12)
  
  #x=x+x
  #y=y+y
  color = (255, 100, 0)
  #pygame.draw.rect(screen, color, pygame.Rect(x, x, y, y))
  #message_display('Test', l1, l2)
  text= []
  for det in i['objects']:
    if(det['name']=='traffic light'):
      
      x = det['x_loc']
      h = 50
      w = 50
      area = det['box_area']
      if(area <=144):
        y = 72
      elif(area >144 and area <= 221):
        y = 216
      elif(area>221 and area <=366):
        y= 504
      else:
        y= 648
      pygame.draw.rect(screen, yellow, [int(x-w), int(y-h), w, h])
     # print([int(x-w), int(y-h), int(x+w), int(y+h)], '  ', x, y)
    
    elif(det['name']=='car'):
      x = det['x_loc']
      h = 70
      w = 70
      h1 = 90
      w1 = 90
      area = det['box_area']
      if(area <=700):
        y = 72
      elif(area >700 and area <= 1596):
        y = 216
      elif(area > 1596 and area <=5498):
        y= 504
      else:
        y= 648
      pygame.draw.rect(screen, blue, [int(x-w), int(y-h), w, h])
      pygame.draw.rect(screen, blue, [int(x-w1), int(y-h1), w1+20, h1+20], 3)
      #print([int(x-w1), int(y-h1), w1, h1], [int(x-w), int(y-h), w, h], '  ', x, y)

    elif(det['name']=='person'):
      color = orange
      x = det['x_loc']
      h = 70
      w = 70
      h1 = 100
      w1 = 100
      area = det['box_area']
      if(area <=292):
        y = 72
      elif(area >292 and area <= 579):
        y = 216
      elif(area > 579 and area <=1570):
        y= 504
      elif(area > 1570 and area <=8640):
        y= 648
      else:
        y=650
        x=0
        w = 1280
        h = 200
        color = red
      pygame.draw.rect(screen, color, [int(x-w), int(y-h), w, h])
      pygame.draw.rect(screen, color, [int(x-w1), int(y-h1), w1+30, h1+30], 3)
      #print([int(x-w1), int(y-h1), w1, h1], [int(x-w), int(y-h), w, h], '  ', x, y)
    
    else:
      t1=dict()
      
      t1['text'] = det['name']
      #t1['XLoc'] = loc[det['x_loc']]
      t1['XLoc'] = det['x_loc']
      #print(t1['XLoc'], det['midX'])
      text.append(t1)
  
  
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
