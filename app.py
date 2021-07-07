from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.uic import *
import os
import sys
from pytube import YouTube, streams

# Main Varabiles


FORM_CLASS,_ = loadUiType(os.path.join(os.path.dirname(__file__), "assets/DesignSYDownloader.ui"))

class MainLoop(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainLoop, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.edit_ui()
        self.connect_buttons()

    def edit_ui(self):
        self.setWindowTitle("SYDownloader")
    
    def connect_buttons(self):
        self.getButton.clicked.connect(self.get_info)
        self.close.clicked.connect(quit)
        self.browseButton.clicked.connect(self.browse)
        self.pushButton_2.clicked.connect(self.download_720p)
        self.pushButton_3.clicked.connect(self.download_360p)

    def browse(self):
        save_location = QFileDialog.getExistingDirectory(self, "Save to")
        self.saveLocationVideo.setText(save_location)

    def get_info(self):
        try:    
            global VIDEO, VIDEO_URL
            VIDEO_URL = self.videoURL.text()
            VIDEO = YouTube(VIDEO_URL)
            title, rating, views, duration = VIDEO.title, f"{round(VIDEO.rating, 1)} ⭐", f"{VIDEO.views} view", f"{round(VIDEO.length/60, 1)} min"
            self.videoTitle.setText(title)
            self.ratingVideo.setText(str(rating))
            self.viewsVideo.setText(str(views))
            self.durationVideo.setText(str(duration))
            return
        except Exception:
            QMessageBox.warning(self, "SYDownloader", "Please Give a valid Url:)")

    def download_360p(self):
        save_location = self.saveLocationVideo.text()
        VIDEO.streams.filter(progressive=True).get_lowest_resolution().download(output_path = save_location)
        self.progress.setText("Downloading")
        VIDEO.register_on_complete_callback(QMessageBox.information(self, "SYDownloader", f"Download Compeleted\n save Location {save_location}"), self.progress.setText("Not Downloading"))

    def download_720p(self):
        save_location = self.saveLocationVideo.text()
        VIDEO.streams.filter(progressive=True).get_lowest_resolution().download(output_path = save_location)
        self.progress.setText("Downloading")
        VIDEO.register_on_complete_callback(QMessageBox.information(self, "SYDownloader", f"Download Compeleted\n save Location {save_location}"), self.progress.setText("Not Downloading"))


def main():
    app = QApplication(sys.argv)
    window = MainLoop()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
