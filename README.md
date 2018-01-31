# object_detection_cv2_tf_dn

OpenCV is used to detect faces or full body on raspberry pi-3.

**Tasks accomplished-**

-Once the webcam detect the face/faces/body for continuously more than 20 frames, an email will be sent using 'smtplib python library' on gmail address signifying that someone has been detected.


-Also in the email there will be links to access real live stream video on browser using 'flask python library'. Flask only let you access live stream on local network.

-Link to access live video stream on global network will also be in sent email. This task requires the use of 'localtunnel(free service) or ngrok(paid service).I haven't tried local tunnel on laptop but haven't tried on raspberry pi. Also global streaming can be pretty slow depending upon the network. localtunnel-https://github.com/localtunnel/localtunnel

-Also when someone will be detected, a message will be sent ot personal registered mobile phone. 'Twilio' has been used to send message to mobile, but needs to register on their website first, and also its a paid service. Twilio gives trial account to test their services.

-A video will also be saved in a directory on raspberry pi(with current date and time), so as to see it later-on.

-Older videos will automatically be deleted. You can delete videos older than may be 5 days. For testing I was deleting videos older than 1 day.

-Dropbox services has been installed on raspberry-pi so that any videos which will be saved in raspberry pi will automaticall be synced to my personal laptop using 'dropbox'. You need to have authentication from 'Dropbox' website also. Link to get dropbox services on raspberry pi- https://www.raspberrypi.org/magpi/dropbox-raspberry-pi/




Will be updating repo for object detection using tensorflow and darknet
