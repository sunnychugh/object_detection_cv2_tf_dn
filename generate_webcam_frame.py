
import cv2

#### only run webcam in one python file,and import current frame wherever needed
camera_port = 0
frame = cv2.VideoCapture(camera_port)

def webcam_frame():
    return frame
