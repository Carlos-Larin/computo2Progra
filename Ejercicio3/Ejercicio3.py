from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QMainWindow, QWidget
from PyQt5.QtGui import QFont, QPalette, QColor
import sys

"""
Ejercicio 3 el lector del nombre y cedula
"""

class Credenciales(QMainWindow):
    def __init__(self):
        super().__init__()

        #Configurar la ventana principal
        self.setWindowTitle("Ejercicio3.ui")
        self.setGeometry(100, 100, 400, 200)

        #Crear el widget central
        basedelBeat = QWidget(self)
        self.setCentralWidget(basedelBeat)

        #Crear los widgets
        self.txtEscriba = QLabel("Escriba aquí", self)
        self.txtnombre = QLabel("Nombre Completo:", self)
        self.txtnumeo = QLabel("Numero de cedula:", self)

        #Personalización de las etiquetas
        self.txtnumeo.setFont(QFont('Arial', 10, QFont.Bold))
        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(255, 0, 0))  # Color rojo para la etiqueta "Numero de cédula"
        self.txtnumeo.setPalette(palette)

        #Crear campos de entrada
        self.intnombre = QLineEdit(self)
        self.intnumero = QLineEdit(self)

        # Crear el botón
        self.btnsubida = QPushButton("Subir Datos", self)
        self.btnsubida.clicked.connect(self.subir_datos)

        #Crear una etiqueta para mostrar el resultado
        self.txtsalida = QLabel(self)
        self.txtsalida.setFont(QFont('Arial', 10, QFont.Bold))

        #Crear el layout en formato de tabla (grid)
        layout = QGridLayout()
        layout.addWidget(self.txtEscriba, 0, 0, 1, 2)  # El texto "Escriba aquí" en la primera fila ocupando 2 columnas
        layout.addWidget(self.txtnombre, 1, 0)  # "Nombre Completo" en la primera columna de la segunda fila
        layout.addWidget(self.intnombre, 1, 1)  # Campo de entrada al lado del texto "Nombre Completo"
        layout.addWidget(self.txtnumeo, 2, 0)  # "Numero de cedula" en la primera columna de la tercera fila
        layout.addWidget(self.intnumero, 2, 1)  # Campo de entrada al lado del texto "Numero de cedula"
        layout.addWidget(self.btnsubida, 3, 0, 1, 2)  # Botón en la cuarta fila, ocupando 2 columnas
        layout.addWidget(self.txtsalida, 4, 0, 1, 2)  # Resultado en la quinta fila, ocupando 2 columnas

        #Asignar el layout al widget central
        basedelBeat.setLayout(layout)

    def subir_datos(self):
        #Obtener los datos ingresados
        nombre = self.intnombre.text()
        cedula = self.intnumero.text()

        #Mostrar los datos en la etiqueta de resultado
        self.txtsalida.setText(f"Nombre: {nombre}, Cédula: {cedula}")


#Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = Credenciales()
ventana.show()
sys.exit(app.exec_())
