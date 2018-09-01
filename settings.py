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
import cv2
from PIL import Image


import pyttsx

engine = pyttsx.init()
engine.say('!!!!settings is opened!')
engine.runAndWait()
playsound('beep.mp3')




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




        now=datetime.now()
        #yr=now.year
        #mnth=now.month
        #dt=now.day
        m=now.minute
        hur=now.hour
        #print h
        #print m

        if(hur<12):
            g="Good morning"
        elif(11<hur|hur<17):
            g = "Good afternoon"
        else:
            g="Good evening"


        engine = pyttsx.init()
        engine.say( '!please wait ! ,until identify your face')
        engine.runAndWait()


        class Eye:
            def my_method(self):
                faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
                cam = cv2.VideoCapture(0);

                engine = pyttsx.init()
                engine.say(
                    'I capture yor face with different angles!,please look at me until i say')
                engine.runAndWait()

                id = 1
                samplenum = 0;
                while (True):

                    ret, img = cam.read();
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:
                        samplenum = samplenum + 1;
                        cv2.imwrite("facecaptured/faceid." + str(id) + "." + str(samplenum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.waitKey(100);
                    cv2.imshow("Face", gray);
                    cv2.waitKey(1);
                    if (samplenum > 10):
                        break
                engine = pyttsx.init()
                engine.say('thanks dude')
                engine.runAndWait()
                cv2.destroyAllWindows()

                engine = pyttsx.init()
                engine.say('I remember your face')
                engine.runAndWait()

                recognizer = cv2.createLBPHFaceRecognizer();
                path = 'facecaptured'

                def getImagesWithID(path):
                    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
                    faces = []
                    IDs = []
                    for imagePath in imagePaths:
                        faceImg = Image.open(imagePath).convert('L');
                        faceNp = np.array(faceImg, 'uint8')
                        ID = int(os.path.split(imagePath)[-1].split('.')[1])
                        faces.append(faceNp)
                        print ID
                        IDs.append(ID)
                        cv2.imshow("training", faceNp)
                        cv2.waitKey(10)
                    return IDs, faces

                Ids, faces = getImagesWithID(path)
                recognizer.train(faces, np.array(Ids))
                recognizer.save('recognizer/trainningData.yml')

                engine = pyttsx.init()
                engine.say('User is changed successfully')
                engine.runAndWait()
                playsound('beep.mp3')

                cam.release()
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
                    id="Driver"

                    engine = pyttsx.init()
                    engine.say('User successfully identified! user is being navigated to face changing process')
                    engine.runAndWait()
                    #engine.say('Today is' + dt + 'of' + mnth + yr + 'time is ')
                    #engine.say(hur)
                    #engine.say(m)
                    #engine.say(tt)
                    #print hur

                    #print "User successfully identified,Welcome Ranga,Your eyes are tracking ,you can begin journey safely"

                    #winsound.PlaySound('Scream+1.wav', winsound.SND_FILENAME)

                    #cv2.waitKey(1000)
                    cam.release()

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
                    if s>20:
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






