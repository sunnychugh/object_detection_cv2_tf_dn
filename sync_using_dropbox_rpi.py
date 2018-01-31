import subprocess

def sync_folder():
    
    upload = "/home/pi/object_detection_cv2_tf_dn/Dropbox-uploader/dropbox_uploader.sh upload /home/pi/object_detection_cv2_tf_dn/dropbox_sync_folder_4_videos/ /"
    print('sync_dropbox_activated')
    subprocess.call ([upload], shell=True)
    print('sync_dropbox_finished')
