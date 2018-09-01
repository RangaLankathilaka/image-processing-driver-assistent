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

engine = pyttsx.init()
engine.say('Please tell me the message you want to send ')
engine.runAndWait()

#Spch.my_speech(self)

class Sphbot:
    def my_speechbot(object):






            def active_listen():
                r = sr.Recognizer()
                with sr.Microphone() as src:
                    audio = r.listen(src)
                msg = ''
            #while 1:
                try:
                    msg = r.recognize_google(audio)

                    resp1 = msg.lower()

                    client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')


                    number = 0711467741


                    message = resp1

                    response = client.send_message({
                        'from': 'Alert',
                        'to': number,
                        'text': message
                    })
                    response = response['messages'][0]
                    if response['status'] == '0':
                        print 'Send message', response['message-id']
                        engine = pyttsx.init()
                        engine.say('message send successfully ')
                        engine.runAndWait()


                    else:
                        print 'Error: ', response['error-text']
                        engine = pyttsx.init()
                        engine.say('message sending failed ')
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


