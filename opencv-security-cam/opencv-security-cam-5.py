import cv2
import numpy as np
import time


#### using to import modules saved in different directory
import sys
sys.path.insert(0, '/home/pi/object_detection_cv2_tf_dn')

#%%
##### save files to dropbox-rpi
import sync_using_dropbox_rpi as sudr
##### smtplib is used to send email notifications
import sending_email_using_smtplib as seus                              
##### twilio is used to send messages to mobile (trial version,paid service)
import sending_messages_using_twilio as smut
#### only run webcam in one python file,and import current frame wherever needed
import generate_webcam_frame as gwf
#### local streaming using flask with multithreading
import local_streaming_using_flask as lsuf
import threading
print('no of threads active: ', threading.active_count())
t1 = threading.Thread(target=lsuf.run_app, name='thread1')
t1.daemon = True
t1.start()


#### global streaming using localtunnel with multithreading
import global_streaming_using_localtunnel as gsul
print('no of threads active: ', threading.active_count())
t2 = threading.Thread(target=gsul.run_global_stream, name='thread2')
t2.daemon = True
t2.start()

#### delete files older than particular no. of days
import delete_old_files as dof
#stored_files_path = "/home/pi/opencv-security-cam"
stored_files_path = "/home/pi/object_detection_cv2_tf_dn/dropbox_sync_folder_4_videos"
older_than_days = 1

print('no of threads active: ', threading.active_count())
t3 = threading.Thread(target=dof.delete_files, name='thread3',args=(stored_files_path, older_than_days))
t3.daemon = True
t3.start()

print('no of threads active: ', threading.active_count())



#%%
import collections

import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))


cap = gwf.webcam_frame()
print(cap.isOpened())

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("test.mp4")
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

time_in_sec = 2  
max_length = 20*time_in_sec   #### multiplied by 20, which is cv2 fps
percent_check_on_store_video_deque = int(0.7 * max_length)
store_video_deque = collections.deque(maxlen = max_length)
for i in range(store_video_deque.maxlen):
    store_video_deque.append(False)
    #print(store_video_deque[i])

index=1
make_new_video_file = True
import os
#dropbox_path = "/home/pi/opencv-security-cam"
dropbox_path = "/home/pi/object_detection_cv2_tf_dn/dropbox_sync_folder_4_videos"

while (cap.isOpened()):
    ret, image_np = cap.read()
#    print(ret)      
    
    
    if (ret==True):
        
        #cv2.imshow('object detection', cv2.resize(image_np, (1200,600)))
          
        #Load a cascade file for detecting faces
        face_cascade = cv2.CascadeClassifier('/home/pi/object_detection_cv2_tf_dn/opencv-security-cam/haarcascade_frontalface_default.xml')
        
        #Convert to grayscale
        gray = cv2.cvtColor(image_np,cv2.COLOR_BGR2GRAY)
        
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        print ("Found "+str(len(faces))+" face(s)")
        
        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image_np,(x,y),(x+w,y+h),(255,255,0),2)
        
    #    #Save the result image
    ##    cv2.imwrite('result.jpg',image_np)
        #cv2.imshow('object detection1', cv2.resize(image_np, (800,600)))
        
       
        if (len(faces)>0):  
            store_video_deque.append(True)
        else:
            store_video_deque.append(False)
        
        true_count = store_video_deque.count(True)
        print(store_video_deque.count(True), percent_check_on_store_video_deque)          
        
        if(true_count > percent_check_on_store_video_deque):
            if(make_new_video_file):
                sudr.sync_folder()
                #video_name = "video"+str(index)+".mp4"   
                video_name = "video_"+str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))+".mp4"
                video_name = os.path.join(dropbox_path, video_name)                
                #### be careful about image shape dimension, must match with last column in cv2.VideoWriter
                out1 = cv2.VideoWriter(video_name,fourcc, 20.0, (cap.read()[1].shape[1],cap.read()[1].shape[0]))
                make_new_video_file = False
                
                cv2.imwrite("image_saved.png",image_np)
                
                #### sending email using smtplib
                seus.attached_text_and_image("image_saved.png")
                #### sending msg using twilio
                ####smut.send_msg()
             
                
            print(video_name)    
            out1.write(image_np)
            #cv2.imshow('object detection2', cv2.resize(image_np, (800,600)))
                
        else:
            
            if not (make_new_video_file):
                index=index+1
                make_new_video_file = True
                #cv2.destroyAllWindows()
    
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break
    else:
        break
 

       
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
out1.release()
seus.quit_server()        
