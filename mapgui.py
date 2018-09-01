

from PyQt4 import QtCore, QtGui
import pyttsx
from playsound import playsound


engine = pyttsx.init()
engine.say('!!!!Connecting to the google map!')
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

class Ui_MainWindow(object):

    def search(self):
        engine = pyttsx.init()
        engine.say('!!!!Please wait!map is loding!')
        engine.runAndWait()
        playsound('beep.mp3')
        #url=self.addresstxt.text()
        self.webView.load(QtCore.QUrl("https://www.google.lk/maps/@6.8012876,80.1455021,13z?hl=en"))

    def search1(self):
        engine = pyttsx.init()
        engine.say('!!!!Please wait!map is loding!')
        engine.runAndWait()
        playsound('beep.mp3')
        #url=self.addresstxt.text()
        self.webView.load(QtCore.QUrl("https://www.google.com/maps/@6.7997961,80.1406956,15z/data=!5m1!1e1"))

    def search2(self):
        engine = pyttsx.init()
        engine.say('!!!!Please wait!map is loding!')
        engine.runAndWait()
        playsound('beep.mp3')
        #url=self.addresstxt.text()
        self.webView.load(QtCore.QUrl("https://www.google.lk/maps/@6.8012876,80.1455021,18347m/data=!3m1!1e3?hl=en"))






    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1397, 854)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 10, 261, 91))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setIcon(QtGui.QIcon('map1.png'))
        self.pushButton.setIconSize(QtCore.QSize(70, 70))

        ######action of map button####
        self.pushButton.clicked.connect(self.search)

        ######################








        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 10, 261, 91))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setIcon(QtGui.QIcon('traffic.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))

        ######action of map button####
        self.pushButton_2.clicked.connect(self.search1)

        ######################



        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 10, 261, 91))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.setIcon(QtGui.QIcon('sat.png'))
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))

        ######action of map button####
        self.pushButton_3.clicked.connect(self.search2)

        ######################


        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-10, 110, 1431, 751))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Map", None))
        self.pushButton.setText(_translate("MainWindow", "Map", None))
        self.pushButton_2.setText(_translate("MainWindow", "Traffic", None))
        self.pushButton_3.setText(_translate("MainWindow", "Satelite", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

