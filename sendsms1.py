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
engine.say('!!!!sms service is activated!')
engine.runAndWait()
playsound('beep.mp3')


client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')
engine = pyttsx.init()
engine.say('!To whom! do you want to send message? ')
engine.runAndWait()

#while 1:
def active_listen():
  r = sr.Recognizer()
  with sr.Microphone() as src:
    audio = r.listen(src)
  msg = ''
  # while 1:
  try:
    msg = r.recognize_google(audio)
    msg1 = r.recognize_google(audio)

    resp1 = msg.lower()
    resp2 = msg1.lower()
    id = "call to mother", "mother"
    if resp1 in (id):

      GE = random.choice(
        ("0711467741", "0711467741"))
      engine = pyttsx.init()
      engine.say(GE)

      engine.runAndWait()
      print GE

      number = GE

      engine = pyttsx.init()
      engine.say('Please tell me the message you want to send ')
      engine.runAndWait()

      id1 = resp2
      if resp2 in (id1):
        tell = random.choice(
          (resp2, resp2))
        engine = pyttsx.init()
        engine.say(tell)

        engine.runAndWait()
        print tell

      message = tell

      response = client.send_message({
        'from': 'DriverAssistent',
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

        # idd = "call to mother", "mother"
    if resp1 not in (id):
      er = random.choice(
        ("Contact not saved", "contact not saved"))
      engine = pyttsx.init()
      engine.say(er)

      engine.runAndWait()
      print er


      # if (resp1 not in (stop) and resp1 not in (you) and resp1 not in (datee) and resp1 not in (
      # time1) and resp1 not in (joke1)
      #   and resp1 not in (how1) and resp1 not in (name) and resp2 not in (builder) and resp1 not in (
      # ato) and resp1 not in (ang)):
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

  finally:
    return msg.lower()


active_listen()




