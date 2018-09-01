

import numpy as np
import cv2
import time
from playsound import playsound
import pyttsx
from datetime import datetime
#import winsound



cv2.destroyAllWindows()
engine = pyttsx.init()
engine.say('!!!!anti sleep mode is activated!')
engine.runAndWait()
playsound('beep.mp3')


cap = cv2.VideoCapture(0)  # 640,480
w = 640
h = 480


rec=cv2.createLBPHFaceRecognizer();
rec.load("eyecascade\\trainningData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:


        faces = cv2.CascadeClassifier('haarcascade_eye.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected = faces.detectMultiScale(frame, 1.3, 5)


        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255 ), 1)
            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
            cv2.circle(frame, (x+w/2, y+h/2),3, (0, 0, 255), 5)

            id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (id == 2):
            id = "close"
            print "eye close";
            playsound('sd.mp3')

        elif(id==1):
            id="open"




                #print 1;


            cv2.cv.PutText(cv2.cv.fromarray(frame), str(id), (x, y + h), font, 255);



        # show picture
        cv2.imshow('frame', frame)
       # cv2.imshow('frame2', pupilFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            # else:
            # break


# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
