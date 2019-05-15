import json

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