import cv2
import numpy as np
from datetime import datetime
import time
#import winsound
import pyttsx
import speech_recognition as sr
import os
import string
from playsound import playsound


cv2.destroyAllWindows()

class Facerec:
    def my_face(self):

        start_time = time.time()
        class Spch:
            def my_speech(self):
                r = sr.Recognizer()
                with sr.Microphone() as src:
                    audio = r.listen(src)
                msg = ''
                try:
                    msg = r.recognize_google(audio)
                    print (msg.lower())
                    resp=msg.lower()
                    if resp in "how are you":
                        print 1

                        cv2.destroyAllWindows()
                        engine = pyttsx.init()
                        engine.say(
                            'Welcome! visitor! Your eyes are tracking !,you can begin journey safely')
                        engine.runAndWait()
                        c = Eye()
                        c.my_method()

                    if resp not in "how are you":
                        print 2
                        playsound('D:\imgprs\Facerec\cyran.mp3')
                        #cv2.imwrite(ss.jpg,img)

                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("Could not request results from Google STT; {0}".format(e))
                except:
                    print("Unknown exception occurred!")
                finally:
                    return msg.lower()





        faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        cam=cv2.VideoCapture(0);
        rec=cv2.createLBPHFaceRecognizer();
        rec.load("recognizer\\trainningData.yml")
        id=0





        engine = pyttsx.init()
        engine.say('!!!!secure mode is activated!')
        engine.runAndWait()
        playsound('beep.mp3')


        class Eye:
            def my_method(self):
                cap = cv2.VideoCapture(0)  # 640,480
                w = 640
                h = 480

                rec = cv2.createLBPHFaceRecognizer();
                rec.load("eyecascade\\trainningData.yml")
                id = 0
                font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 2, 1, 0, 2)

                while (cap.isOpened()):
                    ret, frame = cap.read()
                    if ret == True:

                        faces = cv2.CascadeClassifier('haarcascade_eye.xml')
                        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                        detected = faces.detectMultiScale(frame, 1.3, 5)

                        for (x, y, w, h) in detected:
                            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
                            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255), 1)
                            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
                            cv2.circle(frame, (x + w / 2, y + h / 2), 3, (0, 0, 255), 5)

                            id, conf = rec.predict(gray[y:y + h, x:x + w])

                        if (id == 2):
                            id = "close"
                            print "eye close";
                            #engine = pyttsx.init()
                            #engine.say('hey ! wake up')
                            #engine.runAndWait()
                            playsound('sd.mp3')


                        elif (id == 1):
                            id = "open"





                            # print 1;


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


        #print "please wait ! ,until identify your face"
        #winsound.PlaySound('Scream+1.wav', winsound.SND_FILENAME)
        font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,2)
        while(True):
            ret,img=cam.read();
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in faces:

                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])
                if(id==1):
                    id="Ranga"

                    engine = pyttsx.init()
                    engine.say('User successfully identified!,Welcome!'+id +'! Your eyes are tracking !,you can begin journey safely')
                    engine.runAndWait()
                    #engine.say('Today is' + dt + 'of' + mnth + yr + 'time is ')
                    #engine.say(hur)
                    #engine.say(m)
                    #engine.say(tt)
                    #print hur

                    #print "User successfully identified,Welcome Ranga,Your eyes are tracking ,you can begin journey safely"

                    #winsound.PlaySound('Scream+1.wav', winsound.SND_FILENAME)

                    #cv2.waitKey(1000)
                    cv2.destroyAllWindows()

                    c = Eye()
                    c.my_method()


                    #print  1;


                #print("--- %s seconds ---" % (time.time() - start_time))
                elif(id==3):

                    id="identifying"
                    ms="user can't identify"
                    print ms
                    #print("--- %s seconds ---" % (time.time() - start_time))
                    s=time.time() - start_time
                    if s>20000000000:
                        engine = pyttsx.init()
                        engine.say( 'Can not identify your face!,please tell the password')
                        engine.runAndWait()

                        c = Spch()
                        c.my_speech()


















                            # break

                cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
            cv2.imshow("Face",img);



            if(cv2.waitKey(1)==ord('q')):
                break;
        cam.release()
        cv2.destroyAllWindows()

fac = Facerec()
fac.my_face()






