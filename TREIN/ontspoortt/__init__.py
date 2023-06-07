# This is a INIT file witch means all the "APPS" settings are configured here. 
# Config for the lego hat and the train mobule from the class "PassiveMotor" 
# More info: https://buildhat.readthedocs.io/en/latest/buildhat/passivemotor.html


# import Train en Hat als 1 OBJ
from ontspoortt.Train import Train
train = Train()

# import camera module for stream video and 
from ontspoortt.camera import CameraSystem
cam = CameraSystem()

# Config for Flask webapp (http server/)
from flask import Flask
webapp = Flask(__name__)

from ontspoortt import routes

