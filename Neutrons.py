import random
import math
import time
from matplotlib import pyplot as plt
plt.xlim(0, 200)
plt.ylim(0, 100)

class Neutron():
    
    def __init__(self):
        self.color = ""
        self.position = []
        #self.position = [1, 1]
        self.velocity = []
        #self.velocity = [1, 1]
        self.mass = 1/2000
    
    def positionRandom(self):
        self.position = [random.randint(0,100), random.randint(0,100)]
    
    def velocityRandom(self):
        self.velocity = [random.randint(1,5), random.randint(1,5)]
    
    
    def speed(self):
        self.speed = math.sqrt(((self.velocity[0]**2) + (self.velocity[1]**2)))
        #print(self.speed)
    
    def kineticEnergies(self):
        Neutron.speed(self)
        self.KE = 0.5 * self.mass * (self.speed ** 2)
        print(self.KE)
    
    def update(self):
        
        if self.position[0] + self.velocity[0] >= 200:
            self.velocity[0] = -1 * self.velocity[0]
            self.position[0] = 200
        elif self.position[0] + self.velocity[0] <= 0:
            self.velocity[0] = -1 * self.velocity[0]
            self.position[0] = 0
        else:
            self.position[0] += self.velocity[0]
            
        if self.position[1] + self.velocity[1] >= 100:
            self.velocity[1] = -1 * self.velocity[1]
            self.position[1] = 100
        elif self.position[1] + self.velocity[1] <= 0:
            self.velocity[1] = -1 * self.velocity[1]
            self.position[1] = 0   
        else:
            self.position[1] += self.velocity[1]
        
        
    def tick(self):
        Neutron.update(self)
        print("position: " + str(self.position))
        #print("velocity: " + str(self.velocity))
        plt.plot(self.position[0], self.position[1], marker="o", markerfacecolor = self.color, markeredgecolor = self.color)
        
        time.sleep(0.1)

#will be in separate file:

def collision():
    
    #will need to use conservation of momentum to decide new velocities!!!
    
    neutron1.velocity[0],neutron1.velocity[1] = neutron1.velocity[0] * -1, neutron1.velocity[1] * -1
    neutron2.velocity[0],neutron2.velocity[1] = neutron2.velocity[0] * -1, neutron2.velocity[1] * -1





neutron1 = Neutron()
neutron1.color = "green"
neutron1.position = [1, 50]
neutron1.velocity = [1,0]
neutron2 = Neutron()
neutron2.color = "red"
neutron2.position = [43, 50]
neutron2.velocity = [0, 0]

while True:
    neutron1.tick()

    neutron2.tick()
    
    if neutron1.position == neutron2.position or neutron1.position[0] == neutron2.position[0] + 1 or neutron1.position[0] == neutron2.position[0] - 1:
        if neutron1.position == neutron2.position or neutron1.position[1] == neutron2.position[1] + 1 or neutron1.position[1] == neutron2.position[1] - 1:
            print("ALERT ALERT ALERT")
            collision()
    