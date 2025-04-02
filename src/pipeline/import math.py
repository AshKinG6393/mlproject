import math

def getFare(source,destination):
    route=[['TH','GA','IC','HA'], [800,600,900,1000]]

    fare=0.0
    
    if not (source in route[0] and destination in route[0]):
        print("invalid input")
        exit()
    
    if route[0].index(source) < route[0].index(destination):
        for i in range(route[0].index(source),route[0].index(destination)+1):
            fare+=route[1][i]
    
    elif route[0].index(destination) < route[0].index(source):
        for i in range(route[0].index(source)+1, len(route[0])):
            fare+=route[1][i]
        
        for i in range(0, route[0].index(destination)+1):
            fare+=route[1][i]

    return float(math.ceil(fare*0.005))
    