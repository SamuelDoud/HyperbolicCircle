import matplotlib.pyplot as plt
import math
import decimal
import cmath

Domain = 0
Range = 1
centerIndex = 2
radiusIndex = 3
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
    circle = [0,0,0,0]
    circle[Domain] = xMoved
    circle[Range] = yMoved
    circle[centerIndex] = center
    circle[radiusIndex] = radius
    #Since circles are continous we need to append the first coordinate to the end of  the list so that the plotter will complete thet circle
    #Otherwise the circle is going to have a open spot between the first and last calculated coordiante
    return circle#return the coordinates with the offsets as a list of lists with the offset x list in position 0 and offset y list in position 1; append the center point and radius as well

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
def APrime(A, centerGeodesic, radiusGeodesic, centerGeodesicMajor, radiusGeodesicMajor):
    DistCA = DistancePoints(centerGeodesic, A)
    Cx = centerGeodesic[Domain]
    Cy = centerGeodesic[Range]
    Ax = A[Domain]
    Ay = A[Range]
    slope = Slope(A, centerGeodesic)
    yInt = YInt(centerGeodesic, slope)
    a = slope**2 + 1
    b = (-2*Cx + -2*Cy*slope + 2 * slope * yInt)
    c = -1 * (((radiusGeodesic**2)/(DistCA))**2 - Cx**2 - Cy**2 - yInt**2 + (2*Cy*yInt))
    resultsX = QuadraticEquation(a,b,c)
    point1 = [resultsX[0], slope * resultsX[0] + yInt]
    point2 = [resultsX[1], slope * resultsX[1] + yInt]
    aPrime = Select([point1, point2], radiusGeodesicMajor, centerGeodesicMajor) #finds the a' that is logical from the results of the quadratic equation
    return aPrime
def PlotCircle(circle, format):
    plt.plot(circle[Domain], circle[Range], format)
def PlotLineSegment(Start, End, format):
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
    minorCircle[Domain] = ReorderedX
    minorCircle[Range] = ReorderedY #using the old minor circle's coordinates, insert the coordinates
    return minorCircle
    #cull the values outside of the domain and range
    
    return minorCircle
def InCircle(majorRadius, majorCenter, point): # is this point on or in the circle?
    return DistancePoints(point, majorCenter) <= majorRadius # is the distance of the center to the point less than or equal to the radius?
def GetRadius(circle):
    return circle[radiusIndex]
def GetCenter(circle):
    return circle[centerIndex]
def Slope(point1, point2):
    x1 = point1[Domain]
    y1 = point1[Range]
    x2 = point2[Domain]
    y2 = point2[Range]
    if (x2 == x1):
        return 9999999.9 #a big, near infinite number because dividing by zero below causes a crash, but the limit would be inifinity
    return (y2 - y1) / (x2 - x1)
def YInt(point, slope):
    x = point[Domain]
    y = point[Range]
    b = (y - slope * x)
    return b
def InterceptOfLine(slope1, yInt1, slope2, yInt2):
    #get the intercept point of two, non-parallel lines
    x = (yInt1 - yInt2) / (slope2 - slope1)
    y = slope1 * x + yInt1
    return [x,y]
def InterceptsOfLineBetweenCircleCenters(thisRadius, thisCenter, otherCenter):
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
def PlotPoint(point, format):
    plt.plot(point[Domain], point[Range], format)
def GetPerpendicularSlope(slope):
    if (slope == 0):
        return 10000
    return -1 / slope
def ConvertPointsIntoListOfListXandListY(points):
    xS = []
    yS = []
    for point in range(0, len(points[Domain])):
        xS.append(points[point][Domain])
        yS.append(points[point][Range])
    return [xS, yS]
def PlotPerpendicular(point, slope, format):
    slopePer = GetPerpendicularSlope(slope)
    b = YInt(point,slopePer) #gets the yIntercept of the perpendicular lines
    otherPoint = [0,b] #(0,b) is a known point on this line
    points = [otherPoint, point] #use the yIntercept and the point passed the points to which a line can be drawn through
    XYPlotFormat = ConvertPointsIntoListOfListXandListY(points) #convert the points to a useable format with mathPlotLiib
    plt.plot(XYPlotFormat[Domain], XYPlotFormat[Range], format)#plot those points
def GetGeodesicCircle(radius, circleCenter, precision, point1OnCircle, point2OnCircle, format):
    #check if the points passed are on the circle
    error = 0.1
    if (math.fabs(DistancePoints(circleCenter, point1OnCircle) - DistancePoints(circleCenter, point2OnCircle)) > error or (DistancePoints(point1OnCircle,circleCenter) - radius) > error):
        return "Not points on the circle"
    #calculate the y=mx+b for the tangents of the points on the circle
    slopePoint1Perpendicular = GetPerpendicularSlope(Slope(point1OnCircle, circleCenter))
    slopePoint2Perpendicular = GetPerpendicularSlope(Slope(point2OnCircle, circleCenter))
    yIntPoint1 = YInt(point1OnCircle, slopePoint1Perpendicular)
    yIntPoint2 = YInt(point2OnCircle, slopePoint2Perpendicular)
    #if the tangent's have the same slope then they are parallel and won't intersect
    if (slopePoint1Perpendicular == slopePoint2Perpendicular):
        return "Points are on opposite ends of the circle, no intersection of the tangents is possible"
    intersectionPoint = InterceptOfLine(slopePoint1Perpendicular, yIntPoint1, slopePoint2Perpendicular, yIntPoint2)# this is the intersection point of the tangents
    #debugging line segments
    PlotLineSegment(intersectionPoint,point1OnCircle,"k-")
    PlotLineSegment(intersectionPoint,point2OnCircle,"k-")
    PlotPoint(intersectionPoint, "g-")
    radiusGeodesic = DistancePoints(intersectionPoint, point1OnCircle) #the definition of a radius of a geodesic is distance between the intersection of the
    print(radiusGeodesic)
    #two points' tangent lines and one of those points
    geoDesic = GetCircleCoordinates(intersectionPoint, radiusGeodesic, precision) #makes a circle with the center at intersection point
    geoDesic = TrimCircle(radius, circleCenter, geoDesic)#trim the geodesic circle by taking the major circle's center and radius
    PlotCircle(geoDesic, format)
    return geoDesic
def GetPointOnCircle(circle, index):
    return [circle[Domain][index], circle[Range][index]]
plt.axis([-1.5,1.5,-1.5,1.5])

center = [0,0]
radius = 1
precision = 1000

circle = GetCircleCoordinates(center, radius, precision)
PlotCircle(circle, "b-")


# the form to create a geodesic - serialize this stuff?
pointA = [circle[Domain][100], circle[Range][100]]
pointB = [circle[Domain][800],  circle[Range][800]]
aGeodesicCircle = GetGeodesicCircle(radius, center, precision, pointA, pointB, "r-")

pointC = GetPointOnCircle(aGeodesicCircle, 10)
pointD = GetPointOnCircle(aGeodesicCircle, len(aGeodesicCircle[Domain]) - 100)
SecondGeodesicCircle = GetGeodesicCircle(GetRadius(aGeodesicCircle), GetCenter(aGeodesicCircle), precision, pointC, pointD, "m-")

a = [0,0]
aPrime = APrime(a, GetCenter(aGeodesicCircle),GetRadius(aGeodesicCircle), center, radius)
PlotPoint(a, "yo")
PlotPoint(aPrime, "go")



#ints = InterceptsOfLineBetweenCircleCenters(radius, center, centerGeoDesic)
#aPrime = APrime(a, centerGeoDesic, radiusGeoDesic, center, radius)
#PlotPoint(aPrime, "ko")
#PlotPoint(a, "yo")




plt.show()