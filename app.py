from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
import os
import sys
from pytube import YouTube

# Main Varabiles


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
        self.close.clicked.connect(quit)
    
    def get_info(self):
        try:    
            VIDEO_URL = self.videoURL.text()
            VIDEO = YouTube(VIDEO_URL)
            title, rating, views, duration = VIDEO.title, f"{round(VIDEO.rating, 1)} ⭐", f"{VIDEO.views} view", f"{round(VIDEO.length/60, 2)} min"
            self.videoTitle.setText(title)
            self.ratingVideo.setText(str(rating))
            self.viewsVideo.setText(str(views))
            self.durationVideo.setText(str(duration))
            return
        except Exception:
            QMessageBox.warning(self, "SYDownloader", "Please Give a valid Url:)")


def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
