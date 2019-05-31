import json
import time
import pygame
import sys
import helper

def dunmpToJson(frame_dict, name):
  with open(name+'.json', "w") as write_file:
    json.dump(frame_dict, write_file, indent=4)

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,0))
    return textSurface, textSurface.get_rect()

def message_display(text, x1, x2, screen):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (((x2-x1)/2),(720/2))
    screen.blit(TextSurf, TextRect)

def display_with_lines(text, screen):
  i=0
  for line in text:
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(line['text'], largeText)
    x = line['XLoc']
    TextRect.center = (((x[1]+x[0])/2),(720/2)+(i*20)+(15*i))
    screen.blit(TextSurf,TextRect)
    i+=1

def display_with_linesA(text, screen):
  i=0
  for line in text:
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(line['text'], largeText)
    x = line['XLoc']
    #print(x)
    TextRect.center = (x,(720/2)+(i*20)+(15*i))
    screen.blit(TextSurf,TextRect)
    i+=1

def getXLoc(data):
    x1 = 160
    x2 = 160+160
    x3= 160 + 160 +160
    for i in data:
        for det in i['objects']:
            if det['midX'] < x1:
                det['x_loc'] = 0
            elif (det['midX']<x2  and det['midX']>=x1):
                det['x_loc'] = 1
            elif (det['midX']<x3  and det['midX']>=x2):
                det['x_loc'] =2
    return data

def getXLocA(data):
    # x1 = 160
    # x2 = 160+160
    # x3= 160 + 160 +160
    # for i in data:
    #     for det in i['objects']:
    #         if det['midX'] < x1:
    #             det['x_loc'] = 0
    #         elif (det['midX']<x2  and det['midX']>=x1):
    #             det['x_loc'] = 1
    #         elif (det['midX']<x3  and det['midX']>=x2):
    #             det['x_loc'] =2
    for i in data:
        for det in i['objects']:
            x=det['midX']
            x_loc = int((x/480)*1280)
            det['x_loc'] = x_loc
    return data

def getFrameData(name):
    with open(name, 'r') as f:
        data = json.load(f)

    return (data)

def delPoly(data):
    for i in data:
        del(i['lanePolygon'])
    return (data)

def laneBoundary(pts, poly):
    mi = 10000
    indmin = 0
    ma = -10000
    indmax = 0
    for i in range(len(pts)):
        if pts[i][0] <mi:
            mi = pts[i][0]
            indmin = i
        
        
        
        if pts[i][0] > ma:
            ma = pts[i][0]
            indmax = i    

    min = poly[indmin][0]
    max = poly[indmax][0]
    if(min < 0):
        min = 0
    if (min > 1280):
        min = 1280
    if(max < 0):
        max = 0
    if (max > 1280):
        max = 1280
    return(min, max)
