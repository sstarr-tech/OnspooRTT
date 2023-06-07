from computeserver import server,model
from flask import render_template, redirect, url_for, request, jsonify,flash,send_file,flash,Response
import requests, json, re, io,time,zlib
import numpy as np
from PIL import Image, ImageDraw
import json_numpy
############### vanhetspoor
#     API     #
############### 
@server.route("/")
def home():
    return "SERVER WORKING"

@server.route('/api/compute', methods=['POST'])
def api_computeJPG():
    if request.files.get('image'):
        start_time= time.time()
        img_file = request.files['image']
        img_bytes = img_file.read()
        img = Image.open(io.BytesIO(img_bytes)) #PIL.JpegImagePlugin.JpegImageFile PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1280x720 at
        ai_result = model(img, size=1280)
        print("INF took: ", time.time() - start_time)
        if False:
            # Deze functie return de complete IMG sloom
            array=json.loads(ai_result.pandas().xyxy[0].to_json(orient='records'))
            img1 = ImageDraw.Draw(img)
            ret_json={"D":[],"W":[],"G":[]}
            for A in array:
                boxWaarden=[(int(A['xmin']),int(A['ymin'])),(int(A['xmax']),int(A['ymax']))]
                img1.rectangle(boxWaarden, outline ="green",width=3)
                img1.text(boxWaarden[0],A['name'])
                ret_json['G'].append(A['name'])
            img_array = np.asarray(img)
            ret_json = json_numpy.dumps(img_array)
            print("ready: ", time.time() - start_time,"\n\r")            
            return jsonify({"W":ret_json,"A":array})
        elif True:
            # Deze functie return de ai results
            print("ready: ", time.time() - start_time,"\n\r")  
            print(ai_result.pandas().xyxy[0])
            return ai_result.pandas().xyxy[0].to_json(orient='records')
    else:
        return "ERROR NO IMG FOUND"
