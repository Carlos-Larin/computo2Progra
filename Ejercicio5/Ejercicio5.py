"""
un programa que pueda leer 10 datos caracteristicos de una persona aña pancakes
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
import sys

class PersonaHumana(QMainWindow):
    def __init__(self):
        super().__init__()

        #La ventana principal
        self.setWindowTitle("Datos del Humano")
        self.setGeometry(100, 100, 500, 500)

        #Fondo de la ventana
        fondocolor = QPalette()
        fondocolor.setColor(QPalette.Window, QColor(220, 191, 172))
        self.setPalette(fondocolor)

        #widget base
        labase = QWidget(self)
        self.setCentralWidget(labase)

        #crear los labels
        self.lblNombre = QLabel("Nombres:")
        self.lblApellido = QLabel("Apellidos:")
        self.lblNumero = QLabel("Número de Teléfono:")
        self.lblEdad = QLabel("Edad:")
        self.lblEstatura = QLabel("Estatura:")
        self.lblColorP = QLabel("Color de Piel:")
        self.lblColorCabe = QLabel("Color de Cabello:")
        self.lblDireccion = QLabel("Dirección:")
        self.lblEstado = QLabel("Estado Civil:")
        self.lblOcupacion = QLabel("Ocupación:")

        #crear las entradas de texto
        self.inNombre = QLineEdit()
        self.inApellido = QLineEdit()
        self.inNumero = QLineEdit()
        self.inEdad = QLineEdit()
        self.inEstatura = QLineEdit()
        self.inColorP = QLineEdit()
        self.inColorCabe = QLineEdit()
        self.inDireccion = QLineEdit()
        self.inEstado = QLineEdit()
        self.inOcupacion = QLineEdit()

        #boton para subir datos
        self.btnSubirDatos = QPushButton("Subir Datos")
        self.btnSubirDatos.clicked.connect(self.subirDatos)

        #layout para organizar los widgets
        layout = QGridLayout()

        # Añadir los widgets al layout
        layout.addWidget(self.lblNombre, 0, 0)
        layout.addWidget(self.inNombre, 0, 1)
        layout.addWidget(self.lblApellido, 1, 0)
        layout.addWidget(self.inApellido, 1, 1)
        layout.addWidget(self.lblNumero, 2, 0)
        layout.addWidget(self.inNumero, 2, 1)
        layout.addWidget(self.lblEdad, 3, 0)
        layout.addWidget(self.inEdad, 3, 1)
        layout.addWidget(self.lblEstatura, 4, 0)
        layout.addWidget(self.inEstatura, 4, 1)
        layout.addWidget(self.lblColorP, 5, 0)
        layout.addWidget(self.inColorP, 5, 1)
        layout.addWidget(self.lblColorCabe, 6, 0)
        layout.addWidget(self.inColorCabe, 6, 1)
        layout.addWidget(self.lblDireccion, 7, 0)
        layout.addWidget(self.inDireccion, 7, 1)
        layout.addWidget(self.lblEstado, 8, 0)
        layout.addWidget(self.inEstado, 8, 1)
        layout.addWidget(self.lblOcupacion, 9, 0)
        layout.addWidget(self.inOcupacion, 9, 1)
        layout.addWidget(self.btnSubirDatos, 10, 0, 1, 2)

        # Asignar el layout al widget base
        labase.setLayout(layout)

    def subirDatos(self):
        #registrarlos
        nombre = self.inNombre.text()
        apellido = self.inApellido.text()
        numero = self.inNumero.text()
        edad = self.inEdad.text()
        estatura = self.inEstatura.text()
        color = self.inColorP.text()
        colorCabello = self.inColorCabe.text()
        direccion = self.inDireccion.text()
        estado = self.inEstado.text()
        ocupacion = self.inOcupacion.text()

        #mostrar los datos en un QMessageBox
        datos = (f"Nombre: {nombre}\n"
                 f"Apellido: {apellido}\n"
                 f"Teléfono: {numero}\n"
                 f"Edad: {edad}\n"
                 f"Estatura: {estatura}\n"
                 f"Color de Piel: {color}\n"
                 f"Color de Cabello: {colorCabello}\n"
                 f"Dirección: {direccion}\n"
                 f"Estado Civil: {estado}\n"
                 f"Ocupación: {ocupacion}")

        QMessageBox.information(self, "Datos de la Persona", datos)

#Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = PersonaHumana()
ventana.show()
sys.exit(app.exec_())


        