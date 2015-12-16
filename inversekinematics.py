#inversekinematics.py - inverse kinematics functions
import numpy as np
import math
from kinematics import *

def getDist(e, g):
	x = math.sqrt((e.item(0) - g.item(0))**2 + (e.item(1) - g.item(1))**2 + (e.item(2) - g.item(2))**2)
	#print x
	return x

def getNextPoint(e, g, step):
	m = g - e 
	m = m/getDist(e, g)
	#print m*step
	return m*step

def getIK(theta, e, g, err, step, ddtheta):
	J = getJ(ddtheta, theta)
	J_p =  np.linalg.pinv(J)
	de = getNextPoint(e, g, step)
	dtheta = np.cross(de, J_p)
	theta = theta + dtheta
	#e = getFK(theta)
	return theta

#initializing thetas to 0
theta = np.array([0, 0, 0])
#destination
g = np.matrix([0, 0.15])
e = getFK(theta)
err = 0.25
step = 0.01
ddtheta = (2*math.pi)/1000
#while (getDist(e, g) > err):

print theta
print e
