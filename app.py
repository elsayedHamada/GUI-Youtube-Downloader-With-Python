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
        self.edit_ui()
        self.connect_buttons()

    def edit_ui(self):
        self.setWindowTitle("SYDownloader")
    
    def connect_buttons(self):
        self.getButton.clicked.connect(self.get_info)
    
    def get_info(self):
        video_url = self.videURL.text()
        title, rating, views, duration = "", "", "", ""
        self.videoTitle.setText(title)
        self.ratingVideo.setText(rating)
        self.viewsVideo.setText(views)
        self.durationVideo.setText(duration)
    

def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
