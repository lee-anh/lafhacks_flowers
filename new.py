# face emotion detection in live camera

import cv2
import serial
import time


from deepface import DeepFace

'''
ser = serial.Serial('COM12', 9600, timeout=0.5)


def sub(type):  
  
  try: 
   
    
    
    time.sleep(1.5)
    
    # ser.flush()
    if (type == "neutral"):
        print(ser.write(str(1)))
        #print(ser.write(str(1)))
    if (type == "surprise"):
        print(ser.write(str(2)))
        #print(ser.write(bytes(2)))
    if (type == "happy"):
        print(ser.write(str(3)))
        #print(ser.write(bytes(3)))
    if (type == "sad"):
        print(ser.write(str(4)))
        #print(ser.write(bytes(4)))
    
    
    
    #ser.close()
    #print("closed serial" )
    time.sleep(4)
    #time.sleep(2)
    
    
  except: 
    print("not working")
'''
    

while True:
  face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

  cap = cv2.VideoCapture(0)
  counter = 0; 

  frame_rate = 10
  prev = 0
  ret,frame = cap.read()
  result = DeepFace.analyze(img_path = frame , actions=['emotion'], enforce_detection=False )
 
  
  emotion = result[0]['dominant_emotion']
  print(emotion)
  
  cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
  cv2.imshow('frame',frame)

  if cv2.waitKey(1) & 0xff == ord('q'):
     break
  counter +=1 
  cap.release()
  cv2.destroyAllWindows()
  # sub(emotion)
  
  
  

    