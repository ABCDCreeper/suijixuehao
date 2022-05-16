# This Python file uses the following encoding: utf-8
import sys
from form import *
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import *
from random import randint
from qt_material import *
import os
import configparser


class main(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_randxuehao()
        self.ui.setupUi(self)

        config = configparser.ConfigParser()
        #Ui_randxuehao.setupUi.sc.clicked.connect(onClickButton)
        apply_stylesheet(app, theme='light_blue.xml')




def onAbout():
    msgBoxx = QMessageBox()
    msgBoxx.setText("Maded by Creeper Team,All rights reserved")
    msgBoxx.exec()

def get_num(x):

    msgBoxx = QMessageBox()
    msgBoxx.setText(str(randint(1,int(x))))
    msgBoxx.exec()

if __name__ == "__main__":
    app = QApplication()
    window = main()
    window.show()

    sys.exit(app.exec())
