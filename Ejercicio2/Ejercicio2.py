from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QPushButton, QLineEdit, QVBoxLayout, QLabel)
import sys

class URSS(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Escondete()

    def Escondete(self):
        #aqui x,y,ancho,alto
        self.setGeometry(100, 100, 400, 200) 
        self.setWindowTitle("Ventana de Clave Secreta")
        self.show()

        # Crear un widget central
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Etiqueta para el texto
        self.viñetaTxt = QLabel("Ingresa el mensaje nosotros lo codificamos en idioma Morsa", self)

        # Campo de entrada para la contraseña
        self.EntradaDeDatos = QLineEdit(self)
        self.EntradaDeDatos.setEchoMode(QLineEdit.Password)  # Ocultamos la clave

        # Botón para enviar los datos
        self.bottonSubir = QPushButton("Enviar", self)
        self.bottonSubir.clicked.connect(self.verClave)

        # Disposición vertical
        ventanita = QVBoxLayout()
        ventanita.addWidget(self.viñetaTxt)
        ventanita.addWidget(self.EntradaDeDatos)
        ventanita.addWidget(self.bottonSubir)

        # Configuración de la ventana
        central_widget.setLayout(ventanita)
        self.setWindowTitle("Ventana de Incognito")
        self.show()

    def verClave(self):
        # Imprimir la contraseña en la consola
        password = self.EntradaDeDatos.text()
        print(f"Hemos leido tu mente y sabemos que esta es tu contraseña: {password}")


#para que se abra la ventana
app = QApplication(sys.argv)
ventana = URSS()
ventana.show()
app.exec()    
