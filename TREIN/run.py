#
# < in order to run this file type "python run.py" make sure you are in this directory>
#
#
from ontspoortt import webapp,train,cam

if __name__ == '__main__':
    
    webapp.run(port=8080,host="0.0.0.0",threaded=True)
    
#    
#
#
# in order to run this project you need the folowing: FLask, buildhat, multiprocessing 

# vanhetspoor
#pip3 install Flask
#pip3 install buildhat    
#pip3 install 
#pip3 install tensorflow
