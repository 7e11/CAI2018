import time, calendar
import cv2
import os


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(os.path.dirname(os.path.abspath(__file__)) + '\\faceCascade.xml')

# Define the codec and create VideoWriter object

xvid = cv2.VideoWriter_fourcc(*'XVID')

while True:
    i = str(calendar.timegm(time.gmtime()))
    xvid_out = cv2.VideoWriter('videos/' + i + '.avi', xvid, 30.0, (640, 480))
    for y in range(30 * 15):
        try:
            ret, frame = cap.read()
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

            # Detects faces
            if faces:
                faceDetected = True

        except KeyboardInterrupt:
            # Release everything if job is finished
            cap.release()
            xvid_out.release()
            cv2.destroyAllWindows()
    command = 'ffmpeg -i videos/' + str(i) + '.avi videos/' + str(i) + '.mp4 && python3 upload_file.py ' + str(i)
    os.system(command)
