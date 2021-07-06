from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os
import sys
import pytube

FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname(__file__), "assets/DesignSYDownloader.ui"))

class MainLoop(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainLoop, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
