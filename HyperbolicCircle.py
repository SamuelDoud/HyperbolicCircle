import matplotlib.pyplot as plt
import math
import decimal

domain = 0
range = 1
def GetCircleCoordinates(centerX, centerY,radius, precision):
    x = []
    y = []
    tempX = 0.0
    tempY = 0.0
    radiusSquared = radius * radius
    for i in range(-radius * precision, (radius) * precision): # loops throught from 0 to the radius with a precision
        tempX = (i / precision) # sets the x coordinate with a precision
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
    return [xMoved, yMoved]#return the coordinates with the offsets as a list of lists with the offset x list in position 0 and offset y list in position 1

def Strip(circle, domainOrRange, min, max):
    trimmedDomain = []
    trimmedRange = []
    len(circle[domainOrRange])
    for i in range(0, length):
        #this is an closed interval, ask Tom if the interval should be open
        if circle[domainOrRange][i] > min and circle[domainOrRange][i] < max:
            trimmedDomain.append(circle[0][i])
            trimmedRange.append(circle[0][i])
    trimmedCircle
circle = GetCircleCoordinates(5, 5, 3, 1000)
strippedCircle = Strip(circle, domain, 0, 1)
plt.plot(strippedCircle[domain], strippedCircle[range])
plt.axis([0,10,0,10])
plt.show()