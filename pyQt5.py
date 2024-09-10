import sys
#el sys para ver los datos del sistema

from PyQt5.QtWidgets import (QApplication,QWidget,QMainWindow,QPushButton,
                             QLabel,QVBoxLayout,QLineEdit)

"""
super().__init()
es como herencia padre he hijo
y sirve para llamar al constructor "super()" lo que hace es:
traer todo lo del padre y reemplazarlo en la hija
practicamente un molde,
una exportacion de la propiedad
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class VentanaMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana no de casa")
        # eje x, eje y, ancho, alto
        self.setGeometry(100, 200, 300, 300)
        boton = QPushButton("Haz clic aquí")
        self.setCentralWidget(boton)

# Inicializa la aplicación
app = QApplication(sys.argv)
# Crea una instancia de VentanaMain
ventana = VentanaMain()
ventana.show()
# Ejecuta la aplicación
app.exec()
