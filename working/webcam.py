import numpy as np
import cv2
import os


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object

xvid = cv2.VideoWriter_fourcc(*'XVID')
xvid_out = cv2.VideoWriter('xvid.avi', xvid, 5.0, (640, 480))

i = 0
for x in range(5):
    i += 1
    xvid_out = cv2.VideoWriter('videos/' + str(i) + '.avi', xvid, 10.0, (640, 480))
    for y in range(5 * 30):
        try:
            ret, frame = cap.read()
            xvid_out.write(frame)

        except KeyboardInterrupt:
            # Release everything if job is finished
            cap.release()
            xvid_out.release()
            cv2.destroyAllWindows()
    command = 'ffmpeg -i videos/' + str(i) + '.avi videos/' + str(i) + '.mp4 && node upload.js ' + str(i)
    os.system(command)
