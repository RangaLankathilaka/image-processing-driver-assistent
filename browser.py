# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Mon Jan 15 00:03:34 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
    def back(self):
        print ('back')

    def forward(self):
        print ('for')

    def home(self):
        print ('hm')

    def refresh(self):
        print ('ad')

    def search(self):
        url=self.addresstxt.text()
        self.webView.load(QtCore.QUrl("https://tunein.com/radio/ABC-Hiru-FM-967-s14427/"))

    def goaddress(self):
        print ('gg')





    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1037, 797)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.backbtn = QtGui.QToolButton(self.centralwidget)
        self.backbtn.setGeometry(QtCore.QRect(20, 30, 61, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbtn.setIcon(icon)
        self.backbtn.setIconSize(QtCore.QSize(32, 32))
        self.backbtn.setObjectName(_fromUtf8("backbtn"))

        ######action of back button####
        self.backbtn.clicked.connect(self.back)

        ######################



        self.forwardbtn = QtGui.QToolButton(self.centralwidget)
        self.forwardbtn.setGeometry(QtCore.QRect(90, 30, 61, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.forwardbtn.setIcon(icon1)
        self.forwardbtn.setIconSize(QtCore.QSize(32, 32))
        self.forwardbtn.setObjectName(_fromUtf8("forwardbtn"))

        ######action of back button####
        self.forwardbtn.clicked.connect(self.forward)

        ######################



        self.refreshbtn = QtGui.QToolButton(self.centralwidget)
        self.refreshbtn.setGeometry(QtCore.QRect(160, 30, 61, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Capture1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshbtn.setIcon(icon2)
        self.refreshbtn.setIconSize(QtCore.QSize(32, 32))
        self.refreshbtn.setObjectName(_fromUtf8("refreshbtn"))

        ######action of back button####
        self.refreshbtn.clicked.connect(self.refresh)

        ######################

        self.homebtn = QtGui.QToolButton(self.centralwidget)
        self.homebtn.setGeometry(QtCore.QRect(230, 30, 61, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homebtn.setIcon(icon3)
        self.homebtn.setIconSize(QtCore.QSize(32, 32))
        self.homebtn.setObjectName(_fromUtf8("homebtn"))

        ######action of back button####
        self.homebtn.clicked.connect(self.home)

        ######################

        self.addresstxt = QtGui.QLineEdit(self.centralwidget)
        self.addresstxt.setGeometry(QtCore.QRect(300, 30, 651, 51))
        self.addresstxt.setObjectName(_fromUtf8("addresstxt"))

        ######action of back button####
        #self.addresstxt.clicked.connect(self.goaddress)

        ######################




        self.searchbtn = QtGui.QToolButton(self.centralwidget)
        self.searchbtn.setGeometry(QtCore.QRect(960, 30, 61, 51))

        ######action of back button####
        self.searchbtn.clicked.connect(self.search)

        ######################

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Capture4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchbtn.setIcon(icon4)
        self.searchbtn.setIconSize(QtCore.QSize(32, 32))
        self.searchbtn.setObjectName(_fromUtf8("searchbtn"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(-60, 90, 1101, 711))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.backbtn.setText(_translate("MainWindow", "...", None))
        self.forwardbtn.setText(_translate("MainWindow", "...", None))
        self.refreshbtn.setText(_translate("MainWindow", "...", None))
        self.homebtn.setText(_translate("MainWindow", "...", None))
        self.searchbtn.setText(_translate("MainWindow", "...", None))

from PyQt4 import QtWebKit
#import resource_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

