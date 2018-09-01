import sys
from PyQt4 import QtGui, QtCore
import webbrowser
import pyttsx
from playsound import playsound


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()



    def initUI(self):



        self.lcd = QtGui.QLCDNumber(self)
        self.lcd.setDigitCount(8)  # change the number of digits displayed
        self.lcd.setGeometry(30, 360, 400, 81)
        #self.setWindowTitle('Time')

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.lcd)
        #self.setLayout(vbox)












        btn1 = QtGui.QPushButton("Anti sleep", self)
        btn1.setGeometry(QtCore.QRect(250, 50, 181, 81))
        btn1.setIcon(QtGui.QIcon('eye.png'))
        btn1.setIconSize(QtCore.QSize(50, 50))

        btn2 = QtGui.QPushButton("Voice call", self)
        btn2.setGeometry(QtCore.QRect(250, 160, 181, 81))
        btn2.setIcon(QtGui.QIcon('call.png'))
        btn2.setIconSize(QtCore.QSize(50, 50))

        btn3 = QtGui.QPushButton("Assistent", self)
        btn3.setGeometry(QtCore.QRect(30, 50, 181, 81))
        btn3.setIcon(QtGui.QIcon('bot.png'))
        btn3.setIconSize(QtCore.QSize(50, 50))

        btn4 = QtGui.QPushButton("Map", self)
        btn4.setGeometry(QtCore.QRect(30, 160, 181, 81))
        btn4.setIcon(QtGui.QIcon('map.png'))
        btn4.setIconSize(QtCore.QSize(50, 50))

        btn5 = QtGui.QPushButton("Security", self)
        btn5.setGeometry(QtCore.QRect(470, 50, 181, 81))
        btn5.setIcon(QtGui.QIcon('sec.png'))
        btn5.setIconSize(QtCore.QSize(50, 50))

        btn6 = QtGui.QPushButton("SMS", self)
        btn6.setGeometry(QtCore.QRect(470, 160, 181, 81))
        btn6.setIcon(QtGui.QIcon('sms.png'))
        btn6.setIconSize(QtCore.QSize(50, 50))

        btn7 = QtGui.QPushButton("MP3 Player", self)
        btn7.setGeometry(QtCore.QRect(30, 260, 181, 81))
        btn7.setIcon(QtGui.QIcon('mp3lo.png'))
        btn7.setIconSize(QtCore.QSize(50, 50))

        btn8 = QtGui.QPushButton("Radio", self)
        btn8.setGeometry(QtCore.QRect(250, 260, 181, 81))
        btn8.setIcon(QtGui.QIcon('radio.png'))
        btn8.setIconSize(QtCore.QSize(50, 50))

        btn9 = QtGui.QPushButton("Calendar", self)
        btn9.setGeometry(QtCore.QRect(470, 260, 181, 81))
        btn9.setIcon(QtGui.QIcon('calendar.png'))
        btn9.setIconSize(QtCore.QSize(50, 50))

        btn10 = QtGui.QPushButton("Settings", self)
        btn10.setGeometry(QtCore.QRect(470, 360, 181, 81))
        btn10.setIcon(QtGui.QIcon('settings.png'))
        btn10.setIconSize(QtCore.QSize(50, 50))





        btn1.clicked.connect(self.buttonClicked1)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked3)
        btn4.clicked.connect(self.buttonClicked4)
        btn5.clicked.connect(self.buttonClicked5)
        btn6.clicked.connect(self.buttonClicked6)
        btn7.clicked.connect(self.buttonClicked7)
        btn8.clicked.connect(self.buttonClicked8)
        btn10.clicked.connect(self.buttonClicked10)
        btn9.clicked.connect(self.buttonClicked9)
        #btn4.clicked.connect(self.open_webbrowser)


        self.statusBar()

        self.setGeometry(630, 350, 685, 480)
        self.setWindowTitle('Driver Assistent')
        self.setWindowIcon(QtGui.QIcon('bot.png'))
        self.show()

    def buttonClicked(self):
        import pin.py
        #import AudioPlayer.py
       # AudioPlayer.Start()

    def buttonClicked1(self):
        import eye3.py

    def buttonClicked3(self):
        import  sp.py

    def buttonClicked4(self):
        from mapgui import Ui_MainWindow
        self.window = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonClicked6(self):
        from smsmain import Ui_Radio
        self.window = QtGui.QDialog()
        self.ui = Ui_Radio()
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonClicked7(self):
        from AudioPlayer import AudioPlayer
        self.window = QtGui.QDialog()
        self.ui = AudioPlayer()
        self.ui.setupUi(self.window)
        self.window.show()


    def buttonClicked8(self):
        from radiomain import Ui_Radio
        self.window = QtGui.QDialog()
        self.ui = Ui_Radio()
        self.ui.setupUi(self.window)
        self.window.show()



    def buttonClicked10(self):
        import  settings.py



    def buttonClicked9(self):
        from calendertest import Example
        self.window = QtGui.QDialog()
        self.ui = Example()
        self.ui.setupUi(self.window)
        self.window.show()

    def buttonClicked5(self):
        #print 'ghgjh'
        import security.py

    def openWindow(self):
        self.window=QtGui.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.Winow)
        self.window.show()







    def showlcd(self):
        time = QtCore.QTime.currentTime()
        text = time.toString('hh:mm:ss')


        self.lcd.display(text)















def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
