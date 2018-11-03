import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object

xvid = cv2.VideoWriter_fourcc(*'XVID')
xvid_out = cv2.VideoWriter('xvid.avi', xvid, 5.0, (640, 480))

i = 0
while True:
    i+=1
    xvid_out = cv2.VideoWriter(str(i) + '.avi', xvid, 10.0, (640, 480))
    for x in range(5 * 10):
        try:
            ret, frame = cap.read()
            xvid_out.write(frame)

        except KeyboardInterrupt:
            # Release everything if job is finished
            cap.release()
            xvid_out.release()
            cv2.destroyAllWindows()
