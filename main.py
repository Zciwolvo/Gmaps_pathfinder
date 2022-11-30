"""Program finding the best route by looking at all possible permutations of given points"""
from math import factorial
from itertools import permutations
from progress.bar import ChargingBar
from point import Point

def route(locations, order, N):
    """Function printing best possible route"""
    print("=======================================")
    print("Origin:", locations[0].detailedLocation)
    K = 1
    if N > 2:
        for L in list(order):
            print(f"Point {K}:" ,locations[L].detailedLocation)
            K += 1
    print("Destination:", locations[-1].detailedLocation)
    print("=======================================")

P = int(input("How many points do you need to connect: \n(In case of too many points (>6) program will be drastically slower) \n"))
if P > 1:
    listOfPoints = []
    ADDRESS = str(input("What's your origin?: \n"))
    point = Point(ADDRESS)
    listOfPoints.append(point)
    for _ in range(P-2):
        ADDRESS = str(input("Point: "))
        point = Point(ADDRESS)
        listOfPoints.append(point)
    ADDRESS = str(input("What's your destination?: \n"))
    point = Point(ADDRESS)
    listOfPoints.append(point)
    MINIMUMDIST = 10.e10
    MINIMUMTIME = 10.e10
    orderDIST = ()
    orderTIME = ()
    if len(listOfPoints) > 2:
        perm = [i+1 for i in range(P-2)]
        perms = permutations(perm)
        bar = ChargingBar('Progress', max = factorial(P-2))
        for i in list(perms):
            DIST = 0
            TIME = 0
            for j in range(P-2):
                DIST += listOfPoints[i[j]-1].distanceToX(listOfPoints[i[j]].pointName)
                TIME += listOfPoints[i[j]-1].timeToX(listOfPoints[i[j]].pointName)
            DIST += listOfPoints[i[-1]].distanceToX(listOfPoints[-1].pointName)
            TIME += listOfPoints[i[-1]].timeToX(listOfPoints[-1].pointName)
            if DIST < MINIMUMDIST:
                MINIMUMDIST = DIST
                orderDIST = i
            if TIME < MINIMUMTIME:
                MINIMUMTIME = TIME
                orderTIME = i
            bar.next()
    else:
        bar = ChargingBar('Progress', max = factorial(P-2))
        MINIMUMDIST = listOfPoints[0].distanceToX(listOfPoints[1].pointName)
        MINIMUMTIME = listOfPoints[0].timeToX(listOfPoints[1].pointName)
        orderDIST = (0,1)
        orderTIME = orderDIST
else:
    print("Number of points must be greater than 1!!!")
bar.finish()

print("Distance:",MINIMUMDIST/1000, "km")
print("Time:", MINIMUMTIME/60, "minutes")
print("Shortest Route:")
route(listOfPoints, orderDIST, P)
print("Fastest Route:")
route(listOfPoints, orderTIME, P)
