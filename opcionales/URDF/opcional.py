import pybullet as p
import time
import pybullet_data

urdf_path = "opcional.urdf"

physicsClient = p.connect(p.GUI) #or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")

startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,-3.15])

robotId = p.loadURDF(urdf_path,startPos, startOrientation)

numJoints = p.getNumJoints(robotId)
print("NumJoints: {}".format(numJoints))
for j in range(numJoints):
     print("{} - {}".format(p.getJointInfo(robotId,j)[0], p.getJointInfo(robotId,j)[1].decode("utf-8")))


joint_1 = p.addUserDebugParameter("base2vertical", -1, 1, 0)
joint_2 = p.addUserDebugParameter("vertical2horizontal", -1, 1, 0)

try:
    while True:
        p.stepSimulation()
        time.sleep(1./240.)

        joint_1_value = p.readUserDebugParameter(joint_1)
        joint_2_value = p.readUserDebugParameter(joint_2)
        
        p.setJointMotorControl2(robotId,0, p.VELOCITY_CONTROL, targetVelocity=joint_1_value)
        p.setJointMotorControl2(robotId,1, p.VELOCITY_CONTROL, targetVelocity=joint_2_value)
        
except KeyboardInterrupt:
      pass
	
p.disconnect()    