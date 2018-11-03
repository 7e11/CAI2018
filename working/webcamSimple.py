import cv2
import os

# cascPath = sys.argv[1]
# cascPath = 'faceCascade.xml'
face_cascade = cv2.CascadeClassifier(os.path.dirname(os.path.abspath(__file__)) + '\\faceCascade.xml')
# print(os.path.dirname(os.path.abspath(__file__)) + '\\faceCascade.xml')
# eye_cascade = cv2.CascadeClassifier('C:\\Users\\Evan\\PycharmProjects\\CAI2018\\eyeCascade.xml')
# smile_cascade = cv2K.CascadeClassifier('C:\\Users\\Evan\\PycharmProjects\\CAI2018\\smileCascade.xml')
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

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
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # smile = smile_cascade.detectMultiScale(roi_gray)
        # for (ex, ey, ew, eh) in eyes:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        # for (sx, sy, sw, sh) in smile:
        #     cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()