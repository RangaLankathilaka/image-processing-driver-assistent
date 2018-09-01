import sys
from PyQt4 import QtCore, QtGui
from ChildWindow import ChildWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        QtCore.QTimer.singleShot(5000, self.showChildWindow)


    def showChildWindow(self):
        self.child_win = ChildWindow(self)
        self.child_win.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())