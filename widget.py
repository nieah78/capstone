# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtCore import pyqtSignal, QThread, QFile
from PyQt5.uic import loadUi
from PyQt5 import uic

class Mainapp(QWidget):
    def __init__(self):
        super(Mainapp, self).__init__()
        # self.ui = uic.loadui('home.ui', self)
        home_ui = loadUi("home.ui", self)

        user_ui = loadUi("user.ui", self)
        user_receive_ui = loadUi("user_receive.ui", self)
        user_receive_done_ui = loadUi("user_receive_done.ui", self)

        delivery_ui = loadUi("delivery.ui", self)
        delivery_receive_ui = loadUi("delivery_receive.ui", self)
        delivery_receive_done_ui = loadUi("delivery_receive_done.ui", self)
        delivery_secret_ui = loadUi("delivery_secret.ui", self)
        
        error_ui = loadUi("error.ui", self)
        goodbye_ui = loadUi("goodbye.ui", self)

        

        

    def user_ui(self): # home.ui에서 user_button 누를 시 이동
        a=a
        

if __name__ == "__main__":
    app = QApplication([])
    widget = Mainapp()
    widget.show()
    sys.exit(app.exec_())

