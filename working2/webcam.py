import time, calendar
import cv2
import os


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object

xvid = cv2.VideoWriter_fourcc(*'XVID')

while True:
    i = str(calendar.timegm(time.gmtime()))
    xvid_out = cv2.VideoWriter('videos/' + i + '.avi', xvid, 10.0, (640, 480))
    for y in range(5 * 15):
        try:
            ret, frame = cap.read()
            #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            xvid_out.write(frame)

        except KeyboardInterrupt:
            # Release everything if job is finished
            cap.release()
            xvid_out.release()
            cv2.destroyAllWindows()
    command = 'ffmpeg -i videos/' + str(i) + '.avi videos/' + str(i) + '.mp4 && python3 upload_file.py ' + str(i)
    os.system(command)
