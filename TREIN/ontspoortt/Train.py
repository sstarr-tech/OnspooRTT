
#Train class with had
from buildhat import PassiveMotor,Hat
import json
portArray=["A","B","C","D"]
class Train(object):
    def __init__(self):
        self.hat = Hat()
        self.port = self.findPort()
        self.motor = PassiveMotor(self.port)
        self.speed=0
        self.max_speed=100
        self.low_speed=-100
        self.motor.mode(1)
        
    def findPort(self):
        ArrayoOfPorts = self.hat.get()
        for key, value in ArrayoOfPorts.items(): 
            if value.get('name') == 'PassiveMotor': return key
        raise Exception("train.py = NO MOTOR FOUND")     
        
    def setTrainSpeed(self,NewSpeed):
        if (self.speed+NewSpeed) < self.max_speed and (self.speed+NewSpeed) > self.low_speed: 
            self.speed+=NewSpeed 
            self.motor.start(self.speed)
        else: 
            print(f"train.py = Please provide a valid speed between {self.max_speed} and {self.low_speed} you gave:{NewSpeed}")

    def setNewTrainSpeed(self,NewSpeed):
        if NewSpeed <= self.max_speed and NewSpeed >= self.low_speed: 
            self.speed=NewSpeed 
            self.motor.start(self.speed)
        else: 
            print(f"train.py = Please provide a valid speed between {self.max_speed} and {self.low_speed} you gave:{NewSpeed}")

    def startTrain(self):
        self.motor.start(self.speed)

    def killTrain(self):
        self.motor.stop()

    def getTrainSpeed(self):
        return self.speed
    
    def getInfo(self):
        return f'{self.motor} and {self.speed}'