import requests, re,json,io,time,imutils,json_numpy,base64
import cv2 as cv
import numpy as np
from flask import send_file
from imutils.video.pivideostream import PiVideoStream
from datetime import datetime
from PIL import Image, ImageDraw

#COMPLINK='http://192.168.128.52:6969/api/compute'
COMPLINK='http://10.3.141.77:6969/api/compute'

class CameraSystem(object):
    def __init__(self):
        self.vs = PiVideoStream(resolution=(1280, 720),framerate=30).start()
        self.file_type = ".jpg" 

    def get_frame(self):
    # get raw frame date and return it in self.file_type
        frame = self.vs.read()
        ret, jpeg = cv.imencode(self.file_type, frame)
        self.previous_frame = jpeg
        return jpeg.tobytes()
        
        
    def gen_stream(self):
    #Render the camera frams and stream them to the target
        while True:
            img = self.get_frame()
            yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n\r\n')     
            
    def gen_stream_AI(self):
    # Send frame to render target and get AI info back
        while True:
            img_cam_raw=self.get_frame()
            if False:
                start_time= time.time()
                # Deze werkt maar is sloom :(
                # Bij deze krijg je de photo zelf terug
                response = requests.post(COMPLINK, files={'image': img_cam_raw}).json()
                print("Respons took: ", time.time()-start_time)
                img = json_numpy.loads(response['W']) 
                im = Image.fromarray(img)
                print("Img omzetten: ", time.time()-start_time)
                MEM_CHACE = io.BytesIO()
                im.save(MEM_CHACE, "JPEG")
                print("READY:", time.time()-start_time,"\n\r")
                yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' +  MEM_CHACE.getvalue() + b'\r\n\r\n')
                 
            elif True:
                # Hier moet je de borders nog tekenen  
                start_time= time.time()
                response = requests.post(COMPLINK, files={'image': img_cam_raw}).json()
                print("respons took:", time.time()-start_time)
                pil_img  = Image.open(io.BytesIO(img_cam_raw)) #PIL.JpegImagePlugin.JpegImageFile PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1280x720 at 
                pil_img_draw = ImageDraw.Draw(pil_img)
                for A in response:
                    # Create box 
                    boxWaarden=[(int(A['xmin']),int(A['ymin'])),(int(A['xmax']),int(A['ymax']))]
                    # Apply box
                    pil_img_draw.rectangle(boxWaarden, outline ="black",width=3)
                    pil_img_draw.text(boxWaarden[0],A['name'])
                MEM_CHACE = io.BytesIO()
                pil_img.save(MEM_CHACE, "JPEG") 
                print("READY:", time.time()-start_time,"\n\r")
                yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' +  MEM_CHACE.getvalue() + b'\r\n\r\n')
            elif False:
                # Test functie voor autmaties rijden trijn  
                start_time= time.time()
                response = requests.post(COMPLINK, files={'image': img_cam_raw}).json()
                print("respons took:", time.time()-start_time)
                img  = Image.open(io.BytesIO(img_cam_raw)) #PIL.JpegImagePlugin.JpegImageFile PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1280x720 at 
                img1 = ImageDraw.Draw(img)
                for A in response:
                    # Create box 
                    boxWaarden=[(int(A['xmin']),int(A['ymin'])),(int(A['xmax']),int(A['ymax']))]
                    name = A['name']
                    img1.text(boxWaarden[0],name)
                    if name in stop_array:
                        # IF boxwaarden binnen X falt maak het rood
                        
                        img1.rectangle(boxWaarden, outline ="red",width=3)
                        # ELIF boxwaarden binnen X falt maak het geel
                        img1.rectangle(boxWaarden, outline ="orange",width=2)
                    else:    
                        # ELSE Maak het groen
                        img1.rectangle(boxWaarden, outline ="green",width=1)
                    
                MEM_CHACE = io.BytesIO()
                img.save(MEM_CHACE, "JPEG") 
                print("READY:", time.time()-start_time,"\n\r")
                yield (b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' +  MEM_CHACE.getvalue() + b'\r\n\r\n')
            else:
                yield ( b'--frame\r\n Content-Type: image/jpeg\r\n\r\n' +  IMAGE + b'\r\n\r\n')
            