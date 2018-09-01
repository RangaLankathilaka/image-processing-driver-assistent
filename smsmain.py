
import webbrowser

from PyQt4 import QtCore, QtGui

import pyttsx
from playsound import playsound
import os
import nexmo
import pyttsx
import speech_recognition as sr


engine = pyttsx.init()
engine.say('!!!!sms service is activated!')
engine.runAndWait()
playsound('beep.mp3')



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Radio(object):

    def buttonhiru(self):




            def active_listen():
                engine = pyttsx.init()
                engine.say('Please tell me the message you want to send ')
                engine.runAndWait()
                playsound('beep.mp3')

                r = sr.Recognizer()
                with sr.Microphone() as src:
                    audio = r.listen(src)
                msg = ''
                # while 1:
                try:
                    msg = r.recognize_google(audio)

                    resp1 = msg.lower()

                    client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')

                    number = 94784514723

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
                except sr.RequestError as e:
                    print("Could not request results from Google STT; {0}".format(e))
                    GEb = "System error!,check the internet connection"
                    engine = pyttsx.init()
                    engine.say(GEb)
                    engine.runAndWait()
                except:
                    print("Unknown exception occurred!")
                    GEc = "System error!,check the system"
                    engine = pyttsx.init()
                    engine.say(GEc)
                    engine.runAndWait()
                finally:
                    return msg.lower()

            active_listen()



    def buttonderana(self):
        def active_listen():
            engine = pyttsx.init()
            engine.say('Please tell me the message you want to send ')
            engine.runAndWait()
            playsound('beep.mp3')

            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            msg = ''
            # while 1:
            try:
                msg = r.recognize_google(audio)

                resp1 = msg.lower()

                client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')

                number = 94784514723

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
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}".format(e))
                GEb = "System error!,check the internet connection"
                engine = pyttsx.init()
                engine.say(GEb)
                engine.runAndWait()
            except:
                print("Unknown exception occurred!")
                GEc = "System error!,check the system"
                engine = pyttsx.init()
                engine.say(GEc)
                engine.runAndWait()
            finally:
                return msg.lower()

        active_listen()

    def buttonshree(self):
        def active_listen():
            engine = pyttsx.init()
            engine.say('Please tell me the message you want to send ')
            engine.runAndWait()
            playsound('beep.mp3')

            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            msg = ''
            # while 1:
            try:
                msg = r.recognize_google(audio)

                resp1 = msg.lower()

                client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')

                number = 94784514723

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
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}".format(e))
                GEb = "System error!,check the internet connection"
                engine = pyttsx.init()
                engine.say(GEb)
                engine.runAndWait()
            except:
                print("Unknown exception occurred!")
                GEc = "System error!,check the system"
                engine = pyttsx.init()
                engine.say(GEc)
                engine.runAndWait()
            finally:
                return msg.lower()

        active_listen()



    def buttonshaa(self):
        def active_listen():
            engine = pyttsx.init()
            engine.say('Please tell me the message you want to send ')
            engine.runAndWait()
            playsound('beep.mp3')

            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            msg = ''
            # while 1:
            try:
                msg = r.recognize_google(audio)

                resp1 = msg.lower()

                client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')

                number = 94784514723

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
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}".format(e))
                GEb = "System error!,check the internet connection"
                engine = pyttsx.init()
                engine.say(GEb)
                engine.runAndWait()
            except:
                print("Unknown exception occurred!")
                GEc = "System error!,check the system"
                engine = pyttsx.init()
                engine.say(GEc)
                engine.runAndWait()
            finally:
                return msg.lower()

        active_listen()

    def buttonneth(self):
        def active_listen():
            engine = pyttsx.init()
            engine.say('Please tell me the message you want to send ')
            engine.runAndWait()
            playsound('beep.mp3')

            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            msg = ''
            # while 1:
            try:
                msg = r.recognize_google(audio)

                resp1 = msg.lower()

                client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')

                number = 94784514723

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
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}".format(e))
                GEb = "System error!,check the internet connection"
                engine = pyttsx.init()
                engine.say(GEb)
                engine.runAndWait()
            except:
                print("Unknown exception occurred!")
                GEc = "System error!,check the system"
                engine = pyttsx.init()
                engine.say(GEc)
                engine.runAndWait()
            finally:
                return msg.lower()

        active_listen()

    def buttonsirasa(self):
        client = nexmo.Client(key='64fd0daa', secret='c094860ef6c90264')
        engine = pyttsx.init()
        engine.say('!please tell me the number! want to send message? ')
        engine.runAndWait()
        playsound('beep.mp3')

        # while 1:
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
                        ("94784514723", "94784514723"))
                    engine = pyttsx.init()
                    engine.say(GE)

                    engine.runAndWait()
                    print GE

                    number = GE

                    engine = pyttsx.init()
                    engine.say('Please tell me the message you want to send ')
                    engine.runAndWait()
                    playsound('beep.mp3')

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

    def setupUi(self, Radio):
        Radio.setObjectName(_fromUtf8("Message"))
        Radio.resize(587, 413)
        self.hiru = QtGui.QPushButton(Radio)
        self.hiru.setGeometry(QtCore.QRect(60, 50, 201, 71))
        self.hiru.setObjectName(_fromUtf8("Home"))
        self.hiru.setIcon(QtGui.QIcon('phone.png'))
        self.hiru.setIconSize(QtCore.QSize(70, 70))
        self.hiru.clicked.connect(self.buttonhiru)




        self.derana = QtGui.QPushButton(Radio)
        self.derana.setGeometry(QtCore.QRect(310, 50, 201, 71))
        self.derana.setObjectName(_fromUtf8("contact1"))
        self.derana.setIcon(QtGui.QIcon('mobile.png'))
        self.derana.setIconSize(QtCore.QSize(70, 70))
        self.derana.clicked.connect(self.buttonderana)






        self.shaa = QtGui.QPushButton(Radio)
        self.shaa.setGeometry(QtCore.QRect(310, 160, 201, 71))
        self.shaa.setObjectName(_fromUtf8("contact2"))
        self.shaa.setIcon(QtGui.QIcon('mobile.png'))
        self.shaa.setIconSize(QtCore.QSize(70, 70))
        self.shaa.clicked.connect(self.buttonshaa)




        self.shree = QtGui.QPushButton(Radio)
        self.shree.setGeometry(QtCore.QRect(60, 160, 201, 71))
        self.shree.setObjectName(_fromUtf8("contact3"))
        self.shree.setIcon(QtGui.QIcon('mobile.png'))
        self.shree.setIconSize(QtCore.QSize(70, 70))
        self.shree.clicked.connect(self.buttonshree)



        self.sirasa = QtGui.QPushButton(Radio)
        self.sirasa.setGeometry(QtCore.QRect(310, 270, 201, 71))
        self.sirasa.setObjectName(_fromUtf8("sirasa"))
        self.sirasa.setIcon(QtGui.QIcon('other.png'))
        self.sirasa.setIconSize(QtCore.QSize(50, 50))
        self.sirasa.clicked.connect(self.buttonsirasa)


        self.neth = QtGui.QPushButton(Radio)
        self.neth.setGeometry(QtCore.QRect(60, 270, 201, 71))
        self.neth.setObjectName(_fromUtf8("neth"))
        self.neth.setIcon(QtGui.QIcon('mobile.png'))
        self.neth.setIconSize(QtCore.QSize(70, 70))
        self.neth.clicked.connect(self.buttonneth)

        self.retranslateUi(Radio)
        QtCore.QMetaObject.connectSlotsByName(Radio)

    def retranslateUi(self, Radio):
        Radio.setWindowTitle(_translate("Message", "Message", None))
        self.hiru.setText(_translate("Message", " ", None))
        self.derana.setText(_translate("Message", " ", None))
        self.shaa.setText(_translate("Message", "", None))
        self.shree.setText(_translate("Message", "", None))
        self.sirasa.setText(_translate("Message", "", None))
        self.neth.setText(_translate("Message", "", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Radio = QtGui.QDialog()
    ui = Ui_Radio()
    ui.setupUi(Radio)
    Radio.show()
    sys.exit(app.exec_())

