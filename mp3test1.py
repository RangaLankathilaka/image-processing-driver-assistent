import sys
from PyQt4 import QtGui, QtCore



class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
        self.list()





    def initUI(self):








        btn1 = QtGui.QPushButton("Anti sleep", self)
        btn1.setGeometry(QtCore.QRect(250, 50, 181, 81))
        btn1.setIcon(QtGui.QIcon('eye.png'))

        btn2 = QtGui.QPushButton("Voice call", self)
        btn2.setGeometry(QtCore.QRect(250, 160, 181, 81))
        btn2.setIcon(QtGui.QIcon('call.png'))

        btn3 = QtGui.QPushButton("Assistent", self)
        btn3.setGeometry(QtCore.QRect(30, 50, 181, 81))
        btn3.setIcon(QtGui.QIcon('bot.png'))

        btn4 = QtGui.QPushButton("Map", self)
        btn4.setGeometry(QtCore.QRect(30, 160, 181, 81))
        btn4.setIcon(QtGui.QIcon('map.png'))

        btn5 = QtGui.QPushButton("Security", self)
        btn5.setGeometry(QtCore.QRect(470, 50, 181, 81))
        btn5.setIcon(QtGui.QIcon('sec.png'))

        btn6 = QtGui.QPushButton("SMS", self)
        btn6.setGeometry(QtCore.QRect(470, 160, 181, 81))
        btn6.setIcon(QtGui.QIcon('sms.png'))

        btn7 = QtGui.QPushButton("MP3 Player", self)
        btn7.setGeometry(QtCore.QRect(30, 260, 181, 81))
        btn7.setIcon(QtGui.QIcon('mp3.png'))

        btn8 = QtGui.QPushButton("Radio", self)
        btn8.setGeometry(QtCore.QRect(250, 260, 181, 81))
        btn8.setIcon(QtGui.QIcon('radio.png'))

        btn9 = QtGui.QPushButton("Reverse", self)
        btn9.setGeometry(QtCore.QRect(470, 260, 181, 81))
        btn9.setIcon(QtGui.QIcon('rev.png'))

        btn10 = QtGui.QPushButton("Settings", self)
        btn10.setGeometry(QtCore.QRect(470, 360, 181, 81))
        btn10.setIcon(QtGui.QIcon('settings.png'))





        btn1.clicked.connect(self.buttonClicked1)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked3)
        btn10.clicked.connect(self.buttonClicked10)


        self.statusBar()

        self.setGeometry(630, 350, 685, 480)
        self.setWindowTitle('Driver Assistent')
        self.setWindowIcon(QtGui.QIcon('bot.png'))
        self.show()

    def buttonClicked(self):
        import AudioPlayer.py

    def buttonClicked1(self):
        import eye3.py

    def buttonClicked3(self):
        import  facerec.py

    def buttonClicked7(self):
        import  AudioPlayer.py

    def buttonClicked10(self):
        import  pin.py

    def list(self):

        listWidget = myListWidget()

        # Resize width and height
        listWidget.resize(300, 120)

        listWidget.addItem("Item 1");
        listWidget.addItem("Item 2");
        listWidget.addItem("Item 3");
        listWidget.addItem("Item 4");

        listWidget.setWindowTitle('PyQT QListwidget Demo')
        listWidget.itemClicked.connect(listWidget.Clicked)

        listWidget.show()



















def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()