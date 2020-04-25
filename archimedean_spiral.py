#taken and modified from https://gamedev.stackexchange.com/questions/16745/moving-a-particle-around-an-archimedean-spiral-at-a-constant-speed

#Calculation involved in determining the path of an archimedean spiral - ie the spiral a roomba would take to cover all area inside

import math 
from label_generator import LabelGenerator
from map import Map
import copy

#A class for computations related to an Archimedean Spiral

class Point(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    COUNT = 0

    def __init__(self, X, Y):
        '''Defines x and y variables'''
        self.x = X
        self.y = Y

    def move(self, dx, dy):
        '''Determines where x and y move'''
        self.x = self.x + dx
        self.Y = self.y + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.x, self.y) 


    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

class ArchimedeanSpiral:
    alpha = .5
    epsilon = .00001
    # /**
     # * Computes an approximation of the angle at which an Archimedean Spiral
     # * with the given distance between successive turnings has the given 
     # * arc length.<br>
     # * <br>
     # * Note that the result is computed using an approximation, and not
     # * analytically. 
     # * 
     # * @param alpha The distance between successive turnings
     # * @param arcLength The desired arc length
     # * @param epsilon A value greater than 0 indicating the precision
     # * of the approximation 
     # * @return The angle at which the desired arc length is achieved
     # * @throws IllegalArgumentException If the given arc length is negative
     # * or the given epsilon is not positive
     # */
    def computeAngle(self, arcLength):
        alpha = .5
        epsilon = .00001
        angleRad = math.pi + math.pi
        while (True):
            d = self.computeArcLength(alpha, angleRad) - arcLength
            if (math.fabs(d) <= epsilon):
                return angleRad
            da = alpha * math.sqrt(angleRad * angleRad + 1)
            angleRad -= d / da;

    

    # /**
     # * Computes the arc length of an Archimedean Spiral with the given
     # * parameters
     # * 
     # * @param alpha The distance between successive turnings
     # * @param angleRad The angle, in radians
     # * @return The arc length
     # * @throws IllegalArgumentException If the given alpha is negative
     # */
    def computeArcLength(self, alpha, angleRad):
        u = math.sqrt(1 + angleRad * angleRad)
        v = math.log(angleRad + u)
        return 0.5 * alpha * (angleRad * u + v)
    

    # /**
     # * Compute the point on the Archimedean Spiral for the given parameters.<br>
     # * <br>
     # * If the given result point is <code>null</code>, then a new point will
     # * be created and returned.
     # * 
     # * @param alpha The distance between successive turnings
     # * @param angleRad The angle, in radians
     # * @param result The result point
     # * @return The result point
     # * @throws IllegalArgumentException If the given alpha is negative
     # */
    def computePoint(self, angleRad):
        alpha = .5
        distance = angleRad * alpha
        x = math.sin(angleRad) * distance
        y = math.cos(angleRad) * distance
        result= Point(x,y)
        return result;
    
