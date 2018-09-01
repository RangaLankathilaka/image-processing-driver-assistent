# Identify pupils. Based on beta 1

import numpy as np
import cv2
import time
import winsound

cap = cv2.VideoCapture(0)  # 640,480
w = 640
h = 480
id=raw_input('enter id')
samplenum=0;
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:


        faces = cv2.CascadeClassifier('haarcascade_eye.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected = faces.detectMultiScale(frame, 1.3, 5)



        for (x, y, w, h) in detected:
            samplenum = samplenum + 1;
            cv2.imwrite("eyecaptured/eyeid." + str(id) + "." + str(samplenum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255 ), 1)
            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
            cv2.circle(frame, (x+w/2, y+h/2),3, (0, 0, 255), 5)





        pupilO = frame




        # show picture
        cv2.waitKey(100);
    cv2.imshow("eye", frame);
    cv2.waitKey(1);
    if (samplenum > 1000):
        break

            # else:
            # break


# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
