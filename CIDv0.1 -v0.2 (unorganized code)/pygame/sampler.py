def sampler(turnlimit, delta, threshold):
    if(delta < threshold):
        return([1, 0])
    elif(delta > threshold):
        return([0, 1])
    else:
        return([0, 0])