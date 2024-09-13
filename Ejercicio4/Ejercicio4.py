
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QMainWindow, QWidget
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,QFont,QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,QRadialGradient)
from PyQt5.QtWidgets import *
import sys


"""
Ejercicio 4 el perroj
"""

class mascota(QMainWindow):
    def __init__(self):
        super().__init__()
        #Configurar la ventana principal
        self.setWindowTitle("Ejercicio 4 las mascotas")
        self.geometry(100,100,500,500)

        #Crear el widget central
        basePrincipal = QWidget(self)
        self.setCentralWidget(basePrincipal)
        



