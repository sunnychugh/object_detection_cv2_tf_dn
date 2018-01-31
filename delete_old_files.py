import os
import time
import glob


def delete_files(path, old_days):
    current_time = time.time()
    
    for f in glob.glob(os.path.join(path, 'video_*')):
        creation_time = os.path.getctime(f)
        print(f, '---->>days: ', (current_time-creation_time)//(24*3600))
        
        if (current_time - creation_time) // (24*3600) >= old_days:
            os.remove(f)
            print('{} removed'.format(f))
    
    ##### sleeping the thread for 1 hour        
    time.sleep(3600)


