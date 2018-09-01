import random
import time
import pyttsx
from datetime import datetime
import string
import speech_recognition as sr
import os
from playsound import playsound
import nexmo

engine = pyttsx.init()
engine.say('!!!!Driver assistent mode is activated!')
engine.runAndWait()
playsound('beep.mp3')

#Spch.my_speech(self)

class Sphbot:
    def my_speechbot(object):



        now=datetime.now()
        yr=now.year
        mnth=now.month
        dt=now.day
        m=now.minute
        h=now.hour
        #print h
        #print m
        if(mnth==1):
            mnth="January"
        elif(mnth==2):
            mnth="February"
        elif(mnth==3):
            mnth="March"
        elif(mnth==4):
            mnth="April"
        elif(mnth==5):
            mnth="May"
        elif(mnth==6):
            mnth="June"
        elif(mnth==7):
            mnth="July"
        elif(mnth==8):
            mnth="August"
        elif(mnth==9):
            mnth="September"
        elif(mnth==10):
            mnth="Octomber"
        elif(mnth==11):
            mnth="November"
        else:
            mnth="December"



        if(dt==1):
            dt="1st"
        elif(dt==2):
            dt="second"
        elif(dt==3):
            dt="3rd"
        elif(dt==4):
            dt="4th"
        elif(dt==5):
            dt="5th"
        elif(dt==6):
            dt="6th"
        elif(dt==7):
            dt="7th"
        elif(dt==8):
            dt="8th"
        elif(dt==9):
            dt="9th"
        elif(dt==10):
            dt="10th"
        elif(dt==11):
            dt="11th"

        elif(dt==12):
            dt="12nd"
        elif(dt==13):
            dt="13rd"
        elif(dt==14):
            dt="14th"
        elif(dt==15):
            dt="15th"
        elif(dt==16):
            dt="16th"
        elif(dt==17):
            dt="17th"
        elif(dt==18):
            dt="18th"
        elif(dt==19):
            dt="19th"
        elif(dt==20):
            dt="20th"
        elif(dt==21):
            dt="21th"

        elif(dt==22):
            dt="22nd"
        elif(dt==23):
            dt="23rd"
        elif(dt==24):
            dt="24th"
        elif(dt==25):
            dt="25th"
        elif(dt==26):
            dt="26th"
        elif(dt==27):
            dt="27th"
        elif(dt==28):
            dt="28th"
        elif(dt==29):
            dt="29th"
        elif(dt==30):
            dt="30th"
        elif(dt==31):
            dt="31st"


        if(yr==2016):
            yr="2016"
        elif(yr==2017):
            yr="2017"
        elif(yr==2018):
            yr="2018"
        elif(yr==2019):

            yr="2019"
        elif(yr==2020):
            yr="2020"
        elif(yr==2021):
            yr="2021"

        if(h>11):
            tt="PM"
        else:
            tt="AM"






        while 1:
            def active_listen():
                r = sr.Recognizer()
                with sr.Microphone() as src:
                    audio = r.listen(src)
                msg = ''
            #while 1:
                try:
                    msg = r.recognize_google(audio)

                    resp1 = msg.lower()
                    id = "hello","hi","hey"
                    if resp1 in (id):
                        GE = random.choice(
                            ("hi,what can i do for you", "yes dude", "hey,it's nice to hear your voice", "bro,what's the problem?"))
                        engine = pyttsx.init()
                        engine.say(GE)

                        engine.runAndWait()
                        print GE

                    time1 = "time", "atto time", "what is the time", "time please", "please tell me time", "what is the time please"
                    if resp1 in (time1):
                        engine = pyttsx.init()

                        # engine.say('Today is! ' + dt + 'of!' + mnth + yr + '!time is')
                        engine.say(h)
                        engine.say(m)
                        # engine.say(tt)
                        engine.runAndWait()
                    datee = "date", "atto date", "what is the date", "date please", "please tell me the date", "what is the the please", "today", "today please"
                    if resp1 in (datee):
                        engine = pyttsx.init()

                        engine.say('Today is ' + dt + 'of!' + mnth + yr)
                        engine.runAndWait()

                    name = "what is your name", "name", "your name", "ato mean", "what is your name meaning", "your name meaning", "your name meaning please", "name please", "your name please"
                    if resp1 in (name):
                        engine = pyttsx.init()

                        engine.say('Artificial technology of oral! ,easy reference is a.t.o! atto')
                        engine.runAndWait()

                    builder = "who is your builder", "who is your maker", "who makes you", "who builds you", "who creates you", "who is your creator", "who design you", "who is your designer"
                    if resp1 in (builder):
                        engine = pyttsx.init()

                        engine.say('Ranga Lankathilaka!build me for the CMIS project')
                        engine.runAndWait()

                    you = "who are you", "who is atto", "introduce yourself", "introduce about you", "you"
                    if resp1 in (you):
                        engine = pyttsx.init()

                        engine.say(
                            'I am buliding project for the drivers concentration!,Artificial technology of oral! ,easy reference is a.t.o! atto')
                        engine.runAndWait()

                    joke1 = "tell me a joke", "tell a joke", "tell jokes", "joke", "tell me a joke please", "tell a joke please", "tell jokes please", "joke please"
                    if resp1 in (joke1):
                        engine = pyttsx.init()
                        joke = random.choice(
                            ("hahaha!,are you kidding me", "dude,i am not a joker", "hey dude, am i a joker!,hahaha!",
                             "bro,i am designed for your concentration!,not for your entertainment"))
                        engine.say(joke)
                        engine.runAndWait()

                    how1 = "how are you", "how are you getting on", "how do you do"
                    if resp1 in (how1):
                        engine = pyttsx.init()
                        how = random.choice(
                            ("i am fine ,thank you", "i am keeping well ,thanks", "keeping well,thank you",
                             "fine,thanks for asking"))
                        engine.say(how)
                        engine.runAndWait()
                    ato = "atto", "hi atto", "hey atto"
                    if resp1 in (ato):
                        me = random.choice(("yes bro", "yes dude"))
                        # print GE
                        engine = pyttsx.init()
                        engine.say(me)

                        engine.runAndWait()

                    ang = "angry", "are you angry", "are you angry with me"
                    if resp1 in (ang):
                        an = random.choice(("hahaha ! not at all", "no dude", "hey!,no dude",
                                            "hahaha!  may be"))
                        # print GE
                        engine = pyttsx.init()
                        engine.say(an)

                        engine.runAndWait()



                    mp3 = "mp3", "music", "play musics", "play a music", "play music"
                    if resp1 in (mp3):

                        # print GE
                        playsound('D:\imgprs\Facerec\When.mp3')

                    sms = "send message", "sms", "message","send sms"
                    if resp1 in (sms):
                        # print GE
                        # client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')
                        engine = pyttsx.init()
                        engine.say('To whom do you want to message? ')
                        engine.runAndWait()

                        call = "mom", "dad", "son", "brother", "home"
                        who=raw_input("enter contact");
                        if resp1 in (who):

                            engine1 = pyttsx.init()
                            engine1.say('Please tell me the message you want to send ')
                            engine1.runAndWait()
                            message = raw_input("Enter message ")

                        call = "mom", "dad", "son", "brother", "home"
                        if resp1 in (call):

                            engine1 = pyttsx.init()
                            engine1.say('Please tell me the message you want to send ')
                            engine1.runAndWait()

                            message = raw_input("Enter message ")

                            response = client.send_message({
                                'from': 'Alert',
                                'to': number,
                                'text': message
                            })
                            response = response['messages'][0]
                            if response['status'] == '0':
                                print 'Send message', response['message-id']

                            else:
                                print 'Error: ', response['error-text']













                    stop = "bye atto", "goodbye atto", "see you atto", "good night atto", "atto good night"

                    if resp1 in (stop):

                        sl = random.choice(("see you dude", "i am going to sleep!,bye", "bye! see you again",
                                            "see you"))
                        # print GE
                        engine = pyttsx.init()
                        engine.say(sl)
                        engine.runAndWait()







                   # if (resp1 not in (stop) and resp1 not in (you) and resp1 not in (datee) and resp1 not in (
                    #time1) and resp1 not in (joke1)
                     #   and resp1 not in (how1) and resp1 not in (name) and resp2 not in (builder) and resp1 not in (
                    #ato) and resp1 not in (ang)):
                     #   engine = pyttsx.init()
                      #  engine.say('dude,i am designed for your concentration!,not for your entertainment')
                        # print bye
                       # engine.runAndWait()

                    print (msg.lower())
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                    GEa = "I can't recognize your voice!can you tell it again"
                    engine = pyttsx.init()
                    engine.say(GEa)
                    engine.runAndWait()
                except sr.RequestError as e:
                    print("Could not request results from Google STT; {0}".format(e))
                    GEb = "System error!,check the internet connection"
                    engine = pyttsx.init()
                    engine.say(GEb)
                    engine.runAndWait()
                except :
                    print("Unknown exception occurred!")
                    GEc = "System error!,check the system"
                    engine = pyttsx.init()
                    engine.say(GEc)
                    engine.runAndWait()
                finally:
                    return msg.lower()


            active_listen()
bot =Sphbot()
bot.my_speechbot()


