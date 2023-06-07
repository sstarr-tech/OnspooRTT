import requests, re,json,io,time
#handling webapp routing and API calls
from ontspoortt import webapp,train, camera,cam
from ontspoortt.camera import CameraSystem
from flask import render_template, redirect, url_for, request, jsonify,flash,send_file,flash,Response
import numpy as np

###############
# site routes #
###############
@webapp.route("/")
def home():
    return redirect(url_for('app'))

@webapp.route("/app")
def app():
    return render_template("index.html")

@webapp.route("/ai")
def app_ai():
    return render_template("ai_index.html") 
###############
# API CALLS   #
###############
@webapp.route("/api")
def api_home():
    return "api endpoint found"

@webapp.route("/api/endpoint",methods=['GET', 'POST'] )
def api_endpoint():
    action= request.form['function']
    data =  request.form['DATA']
    return_msg=""
    complete=1
    #Print wat voor een actie de server ontvangen heeft
    print(f"user action: {action} and user data: {data}\n")
    if action == "addSpeed" or  action ==  "lowSpeed": 
        speed= int(data) 
        if type(speed)== int: train.setTrainSpeed(speed)
        else: return_msg = "Train speed needs INT"
    
    elif action == "settrainspeed":
        speed= int(data) 
        if type(speed)== int: train.setNewTrainSpeed(speed)
        else: return_msg = "Train speed needs INT"

    elif action == "start":
        train.startTrain()
        return_msg = "Train started"
        
    elif action == "kill":
        train.killTrain()
        return_msg = "Train killed"    

    elif action == "getspeed":
        return_msg=f"current train speed = {train.getTrainSpeed()}" 

    elif action == "getInfo":
        return_msg=train.getInfo()    

    else: 
        return_msg= "This function was not found" + str(action)
        complete=0

    return jsonify({"complete":complete,"DATA":return_msg})    


@webapp.route("/api/speed/<int:TrainSpeed>")
def api_setspeed(TrainSpeed):
    train.setTrainSpeed(TrainSpeed)
    return jsonify({"status":1,"data":"set train speed to:"+str(TrainSpeed)+" "})

@webapp.route("/api/kill")
def api_killtrain():
    train.killTrain()
    return "train stopt"

@webapp.route("/api/streamvideo")
def api_streamvideo():
# Voor het streamen moet je bytes steuren (0/1)
    return Response(cam.gen_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

@webapp.route("/api/streamAI")
def api_stream_video_ai():
    return Response(cam.gen_stream_AI(), mimetype='multipart/x-mixed-replace; boundary=frame')