import cv2
import numpy as np
import pyttsx
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);


engine = pyttsx.init()
engine.say('I capture yor face with different angles!,please enter id number! ,& look at me until i say')
engine.runAndWait()


id=raw_input('enter id')
samplenum=0;
while (True):

    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        samplenum=samplenum+1;
        cv2.imwrite("facecaptured/faceid."+str(id)+"."+str(samplenum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.waitKey(100);
    cv2.imshow("Face", gray);
    cv2.waitKey(1);
    if(samplenum>100):
        break
engine = pyttsx.init()
engine.say('thanks dude')
engine.runAndWait()






cam.release()
cv2.destroyAllWindows()
