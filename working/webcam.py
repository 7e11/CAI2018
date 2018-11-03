import numpy as np
import cv2
import os


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(os.path.dirname(os.path.abspath(__file__)) + '\\faceCascade.xml')

# Define the codec and create VideoWriter object

xvid = cv2.VideoWriter_fourcc(*'XVID')
xvid_out = cv2.VideoWriter('xvid.avi', xvid, 5.0, (640, 480))

i = 0
for x in range(5):
    i += 1
    xvid_out = cv2.VideoWriter('videos/' + str(i) + '.avi', xvid, 10.0, (640, 480))
    for y in range(5 * 30):
        try:
            faceDetected = False
            ret, frame = cap.read()
            xvid_out.write(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
                # flags=cv2.cv.CV_HAAR_SCALE_IMAGE
            )
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                # If we're in this loop, we have a face detected!
                faceDetected = True
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

        except KeyboardInterrupt:
            # Release everything if job is finished
            cap.release()
            xvid_out.release()
            cv2.destroyAllWindows()
    command = 'ffmpeg -i videos/' + str(i) + '.avi videos/' + str(i) + '.mp4 && node upload.js ' + str(i)
    os.system(command)
