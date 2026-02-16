# Imports do sistema
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QProgressBar, QTableWidget, QTextEdit
from PyQt5 import uic
import sys
import time

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Load the ui file
        uic.loadUi("sistema.ui", self)
        # Show The App
        self.show()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()