#joint index

class Joint:
	length = None
	roation = None

#right arm:

#shoulder:
#pitch:
RSP = Joint()
RSP.length = [0, -0.24, 0]
RSP.rotation = [0, 1, 0]
#roll:
RSR = Joint()
RSR.length = [0,0,0]
RSR.rotation = [1,0,0]
#yaw:
RSY = Joint()
RSY.length = [0,0,0]
RSY.rotation = [0,0,1]

#elbow: 
REP = Joint()
REP.length = [0,0,-0.31]
REP.rotation = [0,1,0]

#wrist:
#pitch:
RWY = Joint()
RWY.legnth = [0,0,-0.31]
RWY.rotation = [0,1,0]
#roll:
RWR = Joint()
RWR.length = [0,0,0]
RWR.rotation = [1,0,0]

#end effector:
RE = Joint()
RE.length = [0,0,-0.13]
RE.rotation = [0,0,0]

#left leg:

#hip:
#yaw:
LHY = Joint()
LHY.length = [0, 0.24, -0.38]
LHY.rotation = [0,0,1]
#roll: 
LHR = Joint()
LHR.length = [0,0,0]
LHR.rotation = [1,0,0]
#pitch:
LHP = Joint()
LHP.length = [0,0,0]
LHP.rotation = [0,1,0]

#knee:
LKP = Joint()
LKP.length = [0,0,-0.33]
LKP.rotation = [0,1,0]

#ankle: 
#pitch: 
LAP = Joint()
LAP.length = [0,0,-0.33]
LAP.rotation = [0,1,0]
#roll: 
LAR = Joint()
LAR.length = [0,0,0]
LAR.rotation = [1,0,0]

#end effector: 
LE = Joint()
LE.length = [0,0,-0.12]
LE.rotation = [0,0,0]

#right leg:

#hip:
#yaw:
RHY = Joint()
RHY.length = [0, -0.24, -0.38]
RHY.rotation = [0,0,1]
#roll: 
RHR = Joint()
RHR.length = [0,0,0]
RHR.rotation = [1,0,0]
#pitch:
RHP = Joint()
RHP.length = [0,0,0]
RHP.rotation = [0,1,0]

#knee:
RKP = Joint()
RKP.length = [0,0,-0.33]
RKP.rotation = [0,1,0]

#ankle: 
#pitch: 
RAP = Joint()
RAP.length = [0,0,-0.33]
RAP.rotation = [0,1,0]
#roll: 
RAR = Joint()
RAR.length = [0,0,0]
RAR.rotation = [1,0,0]

#end effector: 
RE = Joint()
RE.length = [0,0,-0.12]
RE.rotation = [0,0,0]

#arrays containing kinematic chain in order
left_leg = [RHY, RHR, RHP, RKP, RAP, RAR, RE]
right_leg = [RHY, RHR, RHP, RKP, RAP, RAR, RE]
