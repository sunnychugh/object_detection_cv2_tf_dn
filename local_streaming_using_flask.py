import generate_webcam_frame as gwf

from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)


@app.route('/')
def indexx():
    return render_template('index.html')

def get_frame():

    video = gwf.webcam_frame()
    
    while True:
        retval, image = video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n' 
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        #yield frame
    #video.release()

@app.route('/video_feed')
def video_feed():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')

def run_app():
    #### try running on separate thread
    app.run('0.0.0.0', debug=False, threaded=True)
