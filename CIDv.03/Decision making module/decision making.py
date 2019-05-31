import pygame
import time
import random
import sys
import json
from helper import *
from sampler import *

pygame.init()

display_width = 1280
display_height = 720

black = (0,0,0)
white = (255,255,255)

green = (0,200, 0)
grey = (200, 200, 200)
yellow = (222,200,0)
blue = (0,0,200)
red = (200, 0, 0)
orange  = (236, 166, 25)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('dObject1.png')

def drawObjects(data, frame, gameDisplay, limits):
        color = (255, 100, 0)
       
        text= []
        i = data[frame]
        
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
                    
                pygame.draw.rect(gameDisplay, yellow, [int(x-w), int(y-h), w, h])
        #     # print([int(x-w), int(y-h), int(x+w), int(y+h)], '  ', x, y)
            
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
                    temp = dict()
                    temp['name'] = det['name']
                    temp['x1'] = x - w1
                    temp['x2'] = x+w1+20
                    limits.append(temp)
                pygame.draw.rect(gameDisplay, blue, [int(x-w), int(y-h), w, h])
                pygame.draw.rect(gameDisplay, blue, [int(x-w1), int(y-h1), w1+20, h1+20], 3)
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
                    temp = dict()
                    temp['name'] = det['name']
                    temp['x1'] = x - w1
                    temp['x2'] = x+w1+30
                    limits.append(temp)
                else:
                    y=650
                    x=0
                    w = 1280
                    h = 200
                    color = red
                pygame.draw.rect(gameDisplay, color, [int(x-w), int(y-h), w, h])
                pygame.draw.rect(gameDisplay, color, [int(x-w1), int(y-h1), w1+30, h1+30], 3)
            #print([int(x-w1), int(y-h1), w1, h1], [int(x-w), int(y-h), w, h], '  ', x, y)
            
            else:
                t1=dict()
                
                t1['text'] = det['name']
                #t1['XLoc'] = loc[det['x_loc']]
                t1['XLoc'] = det['x_loc']
                #print(t1['XLoc'], det['midX'])
                text.append(t1)
        
        
        display_with_linesA(text, gameDisplay)    
        return limits
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    sys.exit(0)

    #game_loop()
    
    

def crash():
    message_display('You Crashed')
    
def game_loop(dataLen):
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    # thing_startx = random.randrange(0, display_width)
    # thing_starty = -600
    # thing_speed = 7
    # thing_width = 100
    # thing_height = 100
    turnCount = 0
    turnLimit = 10
    frame = 0
    gameExit = False
    reward = 0
    limits = []
    count = 0
    timeOut = 10
    frameRate = 30

    while not gameExit:
        min , max = laneBoundary(data[frame]['lanePts'], data[frame]['lanePolygon'])
        mina = int((min/480)*1280)
        maxa = int(((max-min)/480)*1280)
        maxa = mina+maxa
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                turnCount+=1
                #print(turnCount)
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_SPACE:
                    sys.exit(0)
              

            if event.type == pygame.KEYUP:
                #turnCount+=1
                #print(turnCount)
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        #count = count % 4
        
        if(turnCount >= turnLimit or count>(timeOut*frameRate)):
            turnCount = 0
            frame += 1
            frame = frame % dataLen
            x = (display_width * 0.45)
            print('--------------------------')
            print('reward for frame {}: {}'.format(frame, reward))
            print('--------------------------')
            limits.clear()
            sampled = sampler(turnLimit, x_change, threshold = 0)
            print('--------------------------')
            print('decision flag array', sampled)
            print('--------------------------')
            count = 0
            #print('turn limit reached', frame)
            
        x += x_change
        gameDisplay.fill((0, 0, 0))
        pygame.draw.rect(gameDisplay, grey, [0, 0, 1280, 144], 2)
        pygame.draw.rect(gameDisplay, grey, [0, 0, 1280, 288], 2)
        pygame.draw.rect(gameDisplay, grey, [0, 0, 1280, 432], 2)
        pygame.draw.rect(gameDisplay, grey, [0, 0, 1280, 576], 2)
        pygame.draw.rect(gameDisplay, grey, [0, 0, 1280, 720], 2)
        
        
  #print(int((min/480)*1280),int(((max-min)/480)*1280), min, max-min, count)

        pygame.draw.rect(gameDisplay, green, [int((min/480)*1280), 0, int(((max-min)/480)*1280), 720], 12)
        limits = drawObjects(data, frame, gameDisplay, limits)
        
        #print(maxa, mina, x)

        # things(thingx, thingy, thingw, thingh, color)
        # things(thing_startx, thing_starty, thing_width, thing_height, white)
        # thing_starty += thing_speed
        car(x,y)

        if x > display_width - car_width or x < 0:
            reward -= 10
            print('out of bounds', reward)
        
        for i in limits:
            n = i['name']
            x1 = i['x1']
            x2 = i['x2']
            #print(x1, x2, x)
            if((x + car_width>x1 and x<x2)):
                if (n == 'person'):
                    reward -= 10
                    print('crashed in person', reward)
                if (n == 'car'):
                    reward -= 8
                    print('crashed in car', reward)


        # if thing_starty > display_height:
        #     thing_starty = 0 - thing_height
        #     thing_startx = random.randrange(0,display_width)

        ####
        

        if x > maxa or x < mina :
                #print('x crossover')
            #print(mina, maxa, x)
            reward -= 1
            #print('not in lane', reward)
            

        
        
            
        ####
        count+=1
        pygame.display.update()
        clock.tick(frameRate)



data=dict()
data = helper.getFrameData('city_data_100.json')
#data = helper.delPoly(data)
data = helper.getXLocA(data)

dataLen = len(data)
game_loop(dataLen)
pygame.quit()
sys.exit(0)