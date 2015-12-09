import matplotlib.pyplot as plt
import math
import decimal

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
    for currentX in range(-1 * radius * precision, radius * precision): # loops throught from 0 to the radius with a precision
        tempX = (currentX / precision) # sets the x coordinate with a precision
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
    return sqrt(pow(x1-x2, 2) + pow(y1-y2,2))
def QuadraticEquation(a,b,c):
    discriminant = b**2-4*a*c
    if (discriminant < 0):
        return
    plus = (-1*b + math.sqrt(discriminant)) / (2*a)
    negative = (-1*b - math.sqrt(discriminant)) / (2*a)
    return [plus, negative]
def Select(AprimePlus, AprimeNegative, center, slope):
    #set the coordinates
    Cx = center[Domain]
    Cy = center[Range]
    AprimexPlus = AprimePlus[Domain]
    AprimeyPlus = AprimePlus[Range]
    AprimexNegative = AprimeNegative[Domain]
    AprimeyNegative = AprimeNegative[Range]

    if (slope > 0):
        if (AprimexNegative > Ax and AprimexNegative < Cx and AprimeyNegative > Ay and AprimeyNegative < Cx):
            return [AprimexNegative, AprimeyNegative]
        if (AprimexPlus > Ax and AprimexPlus < Cx and AprimexNegative > Ay and AprimexNegative < Cx):
            return [AprimexPlus, AprimeyPlus]
    if (slope < 0):
        if (AprimexNegative > Cx and AprimexNegative < Ax and AprimeyNegative > Cy and AprimeyNegative > Ay):
            return [AprimexNegative, AprimeyNegative]
        if (AprimeyPlus > Cx and AprimexPlus < Ax and AprimexPlus > Cy and AprimexPlus < Ax):
            return [AprimexPlus, AprimeyPlus]
    return #nothing here
#coordinates are arrays of [x,y]
def APrime(a, center, radius):
    Ax = a[Domain]
    Ay = a[Range]
    Cx = otherCenter[Domain]
    Cy = otherCircle[Range]
    m = (Cy - Ay)/(Cx - Ax)
    if (Ax > Cx):
        m = m * -1 # the slope is the negative in this case
    yInt = -1 * (m * Ax - Ay)
    CA = Distance(Cx, Cy, Ax, Ay)
    #quadratic equation, see scanned notes
    c = -1 * (radius**2 / CA - Cx**2 - Cy**2 + 2*Cy*yInt + yInt**2)
    a = m+1
    b = (2*b)-(2*(Cx+Cy))
    results = QuadraticEquation(a,b,c)
    #calculate Ay's from the two Ax's
    AprimePlus = []
    AprimeNegtive = []
    AprimexPlus = results[0]
    AprimexNegative = results[1]
    AprimeyPlus = slope * AprimexPlus + yInt
    AprimeyNegative = slope * AprimexNegative + yInt
    AprimePlus[Domain] = AprimexPlus
    AprimePlus[Range] = AprimeyPlus
    AprimeNegative[Domain] = AprimexNegative
    AprimeNegative[Range] = AprimeyNegative
    #need a way to determine which value is correct
    #A'x must be in the closed interval of <Ax, Cx>
    #A'y must be in the closed interval of <Ay, Cy>
    #<A, C> may switch if the slope is negative
    return Select(AprimePlus, AprimeNegative, center, m)

def plotCircle(circle, format):
    plt.plot(circle[Domain], circle[Range], format)
def plotLineSegment(Start, End, format):
    plt.plot([Start[Domain], End[Domain]], [Start[Range], End[Range]], format)


plt.axis([0,10,0,10])
center = [5,5]
radius = 3
precision = 1000

circle = GetCircleCoordinates(center, radius, precision)
plotCircle(circle, "b-")

centerGeoDesic = [8,8]
radiusGeoDesic = 2
geoDesicCircle = GetCircleCoordinates(centerGeoDesic, radiusGeoDesic, precision)
plotCircle(geoDesicCircle, "r-")

plotLineSegment(centerGeoDesic, center, "g-")


plt.show()