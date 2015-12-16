#kinematics.py - forward kinematics and jacobian function
from joints import *
import numpy as np
from math import cos, sin, atan2

#calculating rotation matrix:
def getR(theta):
	R_x = np.array([[1,0,0],[0,cos(theta[0]), -sin(theta[0])],[0, sin(theta[0]), cos(theta[0])]])
	R_y = np.array([[cos(theta[1]), 0, sin(theta[1])],[0,1,0],[-sin(theta[1]), 0, cos(theta[1])]])	
	R_z = np.array([[cos(theta[2]), -sin(theta[2]), 0],[sin(theta[2]), -cos(theta[2]), 0],[0,0,1]])
	R = R_x.dot(R_y).dot(R_z)
	#print R
	return R

#calculating transformation matrix: 
def getT(theta, R, leg):
	T_total = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) #identity matrix
 	for i in range(len(leg)):
		T = np.zeros((4,4))
		T[0:3:1, 3] = leg[i].length
		T[0:3:1, 0:3:1] = getR(leg[i].rotation*theta)
		T[3,3] = 1
		T_total = T_total.dot(T)
	#print T_total
	return T_total

#getting position and angles from transformation matrix: 
def getPos(T): 
	P = T[0:3:1, 3] #translation matrix
	R = T[0:3:1, 0:3:1] #rotational matrix
	position = ([0,0,0],[0,0,0]) #xyz and angles
	for i in range(len(position[0])):
		position[0][i] = P[i]
	position[1][0] = atan2(R[2, 1], R[2, 2])
	position[1][1] = atan2(-R[2, 0], R[2,1]**2 + R[2, 2]**2)
	position[1][2] = atan2(R[1,0], R[0,0])
	return position
		
def getFK(theta, leg): 
	position = getPos(getT(theta, getR(theta), leg))	
	print position[0]
	return 	np.array([position[0]])

#calculating the jacobian:
def getJ(ddtheta, theta, leg): 
	J = np.zeros((3, 3))
	e = getFK(theta, leg)
	for i in range(3):
		newTheta = theta
		for j in range(3):
			newTheta[j] = newTheta[j] + ddtheta
			deltaE = getFK(newTheta, leg) - e
			J[i,j] = deltaE.item(i)/ddtheta
			print J
	return J


