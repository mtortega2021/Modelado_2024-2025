import pybullet as p
import pybullet_data
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, 0)  


plane_id = p.loadURDF("plane.urdf")
sphere_start_height = 3
sphere = p.loadURDF("sphere_with_restitution.urdf", [0, 0, sphere_start_height])

g = -9.81  
dt = 1/240 
y_inicial = sphere_start_height
v_inicial = 0  
t = 0 

try:
    while True:
        y = y_inicial + v_inicial * t + 0.5 * g * t**2  
        if y < 0.5:
            y = 0.5  # La esfera tiene un radio de 0.5 por lo tanto cuando nuestra y
                    # sea menor al radio, hacemos que no actualice la posición, para simular
                    # la parada en el suelo.
        p.resetBasePositionAndOrientation(sphere, [0, 0, y], [0, 0, 0, 1])
        p.stepSimulation()
        time.sleep(1./240.)  
        t += dt 
except KeyboardInterrupt:
    pass

p.disconnect()
