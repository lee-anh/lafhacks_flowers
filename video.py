import numpy as np
import cv2 as cv 
from deepface import DeepFace

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors = 5)
    
    for x,y,w,h in face:
        img = cv.rectangle(frame,(x,y),(x+w,y+h), (0,0,255),1)
    try: 
      analyze = DeepFace.analyze(frame,actions=['emotion'])
      print(analyze['dominant_emotion'])
    except:
      print("no face")
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()