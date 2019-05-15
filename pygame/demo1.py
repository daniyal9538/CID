import time
import pygame
import sys
import helper

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,0))
    return textSurface, textSurface.get_rect()

def message_display(text, x1, x2):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (((x2-x1)/2),(720/2))
    screen.blit(TextSurf, TextRect)

def display_with_lines(text):
  i=0
  for line in text:
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(line['text'], largeText)
    x = line['XLoc']
    TextRect.center = (((x[1]+x[0])/2),(720/2)+(i*20)+(15*i))
    screen.blit(TextSurf,TextRect)
    i+=1

def display_with_linesA(text):
  i=0
  for line in text:
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(line['text'], largeText)
    x = line['XLoc']
    #print(x)
    TextRect.center = (x,(720/2)+(i*20)+(15*i))
    screen.blit(TextSurf,TextRect)
    i+=1



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
data = helper.getFrameData('city_data.json')
data = helper.delPoly(data)
data = helper.getXLocA(data)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
for i in data:
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


  display_with_linesA(text)
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
