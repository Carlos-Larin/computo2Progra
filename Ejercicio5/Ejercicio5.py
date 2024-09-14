"""
un programa que pueda leer 10 datos caracteristicos de una persona aña pancakes
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,QGridLayout
from PyQt5.QtGui import QFont, QPalette, QColor
import sys

class personahumana(QMainWindow):
    def __init__(self):
        super().__init__()

        #la windous principal
        self.setWindowTitle("Datos del humano")
        self.setGeometry(100,100,500,500)

        #y para que no se vea tan simple el fondo
        fondocolor=QPalette()
        fondocolor.setColor(QPalette.Window,QColor(220, 191, 172))
        self.setPalette(fondocolor)

        #labase
        labase=QWidget(self)
        self.setCentralWidget(labase)

        #creamos los txtLabel
        self.lblNombre = QLabel("nombres: ") #dato 1
        self.lblApellido = QLabel("Apellidos: ")#dato 2
        self.lblNumero = QLabel("Numero de Telefono: ")#dato 3
        self.lblEdad = QLabel("Edad: ")#dato 4
        self.lblEstatura = QLabel("Estatura: ")#dato 5
        self.lblColorP = QLabel("Color de piel: ")#dato 6
        self.lblColorCabe = QLabel("Color de cabello") #dato 7
        self.lblDireccion = QLabel("Donde vive: ")#dato 8
        self.lblEstado = QLabel("Estado civil: ")#dato 9
        self.lblOcupacion = QLabel("Ocupacion: ") #dato 10
        
         #entradas de datos
        self.inNombre = QLineEdit(self)
        self.inApellido = QLineEdit(self)
        self.inNumero = QLineEdit(self)




#Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = personahumana()
ventana.show()
sys.exit(app.exec_())


        