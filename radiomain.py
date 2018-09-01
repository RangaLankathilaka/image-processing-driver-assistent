
import webbrowser

from PyQt4 import QtCore, QtGui

import pyttsx
from playsound import playsound
import os


engine = pyttsx.init()
engine.say('!!!!radio is activated!')
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
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!hiru fm!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/ABC-Hiru-FM-967-s14427/')


    def buttonderana(self):
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!fm dearana!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/FM-Derana-922-s102016/')

    def buttonshree(self):
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!shree fm!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/Shree-FM-990-s106773/')

    def buttonshaa(self):
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!shaa fm!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/ABC-Shaa-FM-911-s184924/')

    def buttonneth(self):
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!neth fm!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/Neth-FM-950-s81656/')

    def buttonsirasa(self):
        os.system("taskkill /im firefox.exe /f")
        engine = pyttsx.init()
        engine.say('!!!!sirasa fm!')
        engine.runAndWait()
        playsound('beep.mp3')

        webbrowser.open('https://tunein.com/radio/Sirasa-FM-1065-s25231/')




    def setupUi(self, Radio):
        Radio.setObjectName(_fromUtf8("Radio"))
        Radio.resize(587, 413)
        self.hiru = QtGui.QPushButton(Radio)
        self.hiru.setGeometry(QtCore.QRect(60, 50, 201, 71))
        self.hiru.setObjectName(_fromUtf8("hiru"))
        self.hiru.setIcon(QtGui.QIcon('hiru.png'))
        self.hiru.setIconSize(QtCore.QSize(70, 70))
        self.hiru.clicked.connect(self.buttonhiru)




        self.derana = QtGui.QPushButton(Radio)
        self.derana.setGeometry(QtCore.QRect(310, 50, 201, 71))
        self.derana.setObjectName(_fromUtf8("derana"))
        self.derana.setIcon(QtGui.QIcon('derana.png'))
        self.derana.setIconSize(QtCore.QSize(70, 70))
        self.derana.clicked.connect(self.buttonderana)






        self.shaa = QtGui.QPushButton(Radio)
        self.shaa.setGeometry(QtCore.QRect(310, 160, 201, 71))
        self.shaa.setObjectName(_fromUtf8("shaa"))
        self.shaa.setIcon(QtGui.QIcon('shaa.png'))
        self.shaa.setIconSize(QtCore.QSize(70, 70))
        self.shaa.clicked.connect(self.buttonshaa)




        self.shree = QtGui.QPushButton(Radio)
        self.shree.setGeometry(QtCore.QRect(60, 160, 201, 71))
        self.shree.setObjectName(_fromUtf8("shree"))
        self.shree.setIcon(QtGui.QIcon('shree.png'))
        self.shree.setIconSize(QtCore.QSize(70, 70))
        self.shree.clicked.connect(self.buttonshree)



        self.sirasa = QtGui.QPushButton(Radio)
        self.sirasa.setGeometry(QtCore.QRect(310, 270, 201, 71))
        self.sirasa.setObjectName(_fromUtf8("sirasa"))
        self.sirasa.setIcon(QtGui.QIcon('sirasa.png'))
        self.sirasa.setIconSize(QtCore.QSize(70, 70))
        self.sirasa.clicked.connect(self.buttonsirasa)


        self.neth = QtGui.QPushButton(Radio)
        self.neth.setGeometry(QtCore.QRect(60, 270, 201, 71))
        self.neth.setObjectName(_fromUtf8("neth"))
        self.neth.setIcon(QtGui.QIcon('neth.png'))
        self.neth.setIconSize(QtCore.QSize(70, 70))
        self.neth.clicked.connect(self.buttonneth)

        self.retranslateUi(Radio)
        QtCore.QMetaObject.connectSlotsByName(Radio)

    def retranslateUi(self, Radio):
        Radio.setWindowTitle(_translate("Radio", "Radio", None))
        self.hiru.setText(_translate("Radio", " ", None))
        self.derana.setText(_translate("Radio", " ", None))
        self.shaa.setText(_translate("Radio", "", None))
        self.shree.setText(_translate("Radio", "", None))
        self.sirasa.setText(_translate("Radio", "", None))
        self.neth.setText(_translate("Radio", "", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Radio = QtGui.QDialog()
    ui = Ui_Radio()
    ui.setupUi(Radio)
    Radio.show()
    sys.exit(app.exec_())

