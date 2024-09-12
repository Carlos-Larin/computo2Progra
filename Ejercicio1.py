from PyQt5.QtWidgets import  (QApplication,QWidget,QMainWindow,
                              QPushButton,QLabel,QVBoxLayout,QLineEdit)
import sys
from PyQt5 import uic

"""
1.Construir un programa que muestre una ventana el cual muestre los nombres y edades centrados
"""
#from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QGridLayout,QFormLayout

class ventanaNoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ejercicio1.ui",self)
      

app = QApplication(sys.argv)
ventana = ventanaNoWindow()
ventana.show()
app.exec()