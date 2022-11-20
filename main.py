import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from design import Ui_weather_form
import requests as req


class MainWindow(QtWidgets.QMainWindow, Ui_weather_form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.init_UI()
        self.frame.setStyleSheet("background-image: url(images/back.jpg);")

    def init_UI(self):
        self.setWindowIcon(QIcon('images/icon.png'))


app = QtWidgets.QApplication([])

application = MainWindow()
ui = Ui_weather_form()
application.show()

sys.exit(app.exec_())
