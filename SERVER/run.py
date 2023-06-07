'''
Based on the code proved by YOLOV5 "restapi.py"

Simple compute server for the OnstpooRTT project, to handel some off the load.

Note this server is in no way secure !
'''
from computeserver import server,model

if __name__ == '__main__':

    server.run(port=6969,host="0.0.0.0",threaded=True,debug=True)
    
#    
#
#
# This project assums you have a working version of YOLOV5 object detection working 
# 
#pip3 install Flask