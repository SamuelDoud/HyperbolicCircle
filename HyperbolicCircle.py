import matplotlib.pyplot as plt
import math
import decimal
import cmath

Domain = 0
Range = 1
def GetCircleCoordinates(center,radius, precision):
    #set the variables
    centerX = center[Domain]
    centerY = center[Range]
    x = []
    y = []
    tempX = 0.0
    tempY = 0.0
    radiusSquared = radius * radius
    for step in range(-1 * precision, precision): # loops throught from 0 to the radius with a precision
        tempX = ((step * radius) / precision) # sets the x coordinate with a precision
        tempY = math.sqrt(radiusSquared - math.pow(tempX, 2)) # calculates the value of y given a radius and a known x coordinate
        x.append(tempX)
        y.append(tempY) #place the calculated values in the array
    xWithPositivesStart= list(x)
    xWithPositivesStart.reverse()
    x.extend(xWithPositivesStart)
    reversedY = list(y)
    reversedY.reverse
    for i in reversedY:
        y.append(i * -1) #add the negative value to the array while also reversing it
    yMoved = []
    xMoved = []
    #these loops below iterate through the lists of x and y and apply the offsets passed to them
    for baseX in x:
        xMoved.append(baseX + centerX)
    for baseY in y:
        yMoved.append(baseY + centerY)
    xMoved.append(xMoved[0])
    yMoved.append(yMoved[0])
    #Since circles are continous we need to append the first coordinate to the end of  the list so that the plotter will complete thet circle
    #Otherwise the circle is going to have a open spot between the first and last calculated coordiante
    return [xMoved, yMoved]#return the coordinates with the offsets as a list of lists with the offset x list in position 0 and offset y list in position 1

def Strip(circle, domainOrRange, min, max):
    trimmedDomain = []
    trimmedRange = []
    length = len(circle[domainOrRange])
    for i in range(0, length):
        #this is an closed interval, ask Tom if the interval should be open
        x = circle[domainOrRange][i]
        if circle[domainOrRange][i] > min and circle[domainOrRange][i] < max:
            trimmedDomain.append(circle[Domain][i])
            trimmedRange.append(circle[Range][i])
    return [trimmedDomain, trimmedRange]
#OA and A'O
def Distance(x1,y1,x2,y2):
    return math.sqrt(pow(x1-x2, 2) + pow(y1-y2,2))
def QuadraticEquation(a,b,c):
    discriminant = b**2 - 4*a*c
    plus = (-1*b + math.sqrt(discriminant)) / (2*a)
    negative = (-1*b - math.sqrt(discriminant)) / (2*a)
    return [plus, negative]
def Select(SolutionsFromQuadratic, circleRadius, circleCenter):
    for point in SolutionsFromQuadratic:
        if InCircle(circleRadius, circleCenter, point):
            return point
    return none
#coordinates are arrays of [x,y]
def APrime(A, center, radius, centerMajor, radiusMajor):
    DistCA = DistancePoints(center, A)
    Cx = center[Domain]
    Cy = center[Range]
    Ax = A[Domain]
    Ay = A[Range]
    slope = Slope(A, center)
    yInt = YInt(center, slope)
    a = slope**2 + 1
    b = (-2*Cx + -2*Cy*slope + 2 * slope * yInt)
    c = -1 * (((radius**2)/(DistCA))**2 - Cx**2 - Cy**2 - yInt**2 + (2*Cy*yInt))
    resultsX = QuadraticEquation(a,b,c)
    point1 = [resultsX[0], slope * resultsX[0] + yInt]
    point2 = [resultsX[1], slope * resultsX[1] + yInt]
    return Select([point1, point2], radiusMajor, centerMajor)
def plotCircle(circle, format):
    plt.plot(circle[Domain], circle[Range], format)
def plotLineSegment(Start, End, format):
    plt.plot([Start[Domain], End[Domain]], [Start[Range], End[Range]], format)
def DistancePoints(Coordinate1, Coordinate2):
    return Distance(Coordinate1[Domain], Coordinate1[Range], Coordinate2[Domain], Coordinate2[Range])
def TrimCircle(majorRadius, majorCenter, minorCircle):
    trimmedMinorCircleX = []
    trimmedMinorCircleY = []
    ReorderedX = []
    ReorderedY = []
    maxDistance = 0
    intercepts = [0,0]
    length = len(minorCircle[0])
    for point in range(0, length):
        #intercepts have the longest distance
        if InCircle(majorRadius, majorCenter, [minorCircle[Domain][point], minorCircle[Range][point]]):# is the "point" in the circle
            trimmedMinorCircleX.append(minorCircle[Domain][point])
            trimmedMinorCircleY.append(minorCircle[Range][point]) #add the point to the trimmed lists
        #order the array by the intercepts
        #intercepts are the points with the longest distance!
    for point in range(0, len(trimmedMinorCircleX)):
        point1 = [trimmedMinorCircleX[point], trimmedMinorCircleY[point]]
        point2 = [trimmedMinorCircleX[(point - 1) % len(trimmedMinorCircleX)], trimmedMinorCircleY[(point - 1) % len(trimmedMinorCircleY)]]
        thisDistance = DistancePoints(point1, point2)
        if (thisDistance > maxDistance):
            maxDistance = thisDistance
            intercepts[0] = (point - 1) % len(trimmedMinorCircleX)
            intercepts[1] = point
    for point in range(intercepts[1], intercepts[0]):
        ReorderedX.append(trimmedMinorCircleX[point])
        ReorderedY.append(trimmedMinorCircleY[point])
    return [ReorderedX, ReorderedY]
    #cull the values outside of the domain and range
    
    return minorCircle
def InCircle(majorRadius, majorCenter, point): # is this point on or in the circle?
    return DistancePoints(point, majorCenter) <= majorRadius # is the distance of the center to the point less than or equal to the radius?
def GetRadius(majorRadius, majorCenter):
    return (circle[Domain][(len(circle[0]) - 1) // 2] - circle[Domain][0]) / 2
def GetCenter(circle):
    length = len(circle[0])
    return [(circle[Domain][(length - 1) // 2] + circle[Domain][0]) / 2, (circle[Range][(length - 1) * 3 //4] + circle[Range][(length - 1) //4]) / 2]
def Slope(point1, point2):
    x1 = point1[Domain]
    y1 = point1[Range]
    x2 = point2[Domain]
    y2 = point2[Range]
    return (y2 - y1) / (x2 - x1)
def YInt(point, slope):
    x = point[Domain]
    y = point[Range]
    return (y - slope * x)
def Intercepts(thisRadius, thisCenter, otherCenter):
    m = Slope(thisCenter, otherCenter)
    yInt = YInt(thisCenter, m)
    a = (m**2+1)
    b = 2*m*yInt
    c = -1*(thisRadius**2 - yInt**2)
    resultsX = QuadraticEquation(a,b,c)
    resultsY = []
    resultsY.append(m * resultsX[0] + yInt)
    resultsY.append(m * resultsX[1] + yInt)
    return [[resultsX[0], resultsY[0]], [resultsX[1], resultsY[1]]]
plt.axis([-5,5,-5,5])
center = [0,0]
radius = 1
precision = 1000
centerGeoDesic = [1,-1 * math.sqrt(3)]
radiusGeoDesic = math.sqrt(3)



circle = GetCircleCoordinates(center, radius, precision)
plotCircle(circle, "b-")
ints = Intercepts(radius, center, centerGeoDesic)
point1 = ints[0]
point2 = ints[1]
a = [.5,.5]

aPrime = APrime(a, centerGeoDesic, radiusGeoDesic, center, radius)

geoDesicCircle = GetCircleCoordinates(centerGeoDesic, radiusGeoDesic, precision)
geoDesicCircle = TrimCircle(radius, center, geoDesicCircle)



plotCircle(geoDesicCircle, "r-")
plotLineSegment(centerGeoDesic, center, "g-")
plotLineSegment(aPrime, centerGeoDesic, "m-")
plt.plot([a[Domain]],[a[Range]], "yo")
plt.plot(aPrime[Domain], aPrime[Range], "ko")
plt.plot([point2[Domain]],[point2[Range]], "ro")


plt.show()