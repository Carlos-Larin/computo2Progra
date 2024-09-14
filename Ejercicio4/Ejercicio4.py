

"""
Ejercicio 4 el perroj
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QListWidget, QVBoxLayout, QHBoxLayout,QGridLayout
from PyQt5.QtGui import QFont, QPalette, QColor
import sys

class firulais(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configurar la ventana principal
        self.setWindowTitle("Ejercicio 4 - Las mascotas")
        self.setGeometry(100, 100, 500, 400)

        #y para que no se vea tan simple el fondo
        fondocolor=QPalette()
        fondocolor.setColor(QPalette.Window,QColor(4, 4, 4 ))
        self.setPalette(fondocolor)

        #crear el widget central
        basePrincipal = QWidget(self)
        self.setCentralWidget(basePrincipal)
        
        #crear los widgets
        self.Dato1 = QLabel("Dato 1 de la mascota", self)
        self.Dato2 = QLabel("Dato 2 de la mascota", self)
        self.Dato3 = QLabel("Dato 3 de la mascota", self)

        #personalización de las etiquetas
        self.Dato1.setFont(QFont('Arial', 10, QFont.Bold))
        self.Dato2.setFont(QFont('Arial', 10, QFont.Bold))
        self.Dato3.setFont(QFont('Arial', 10, QFont.Bold))

        palette = QPalette()
        palette.setColor(QPalette.WindowText, QColor(237, 46, 27 ))  # Color verde para la etiqueta "datos"
        self.Dato1.setPalette(palette)
        self.Dato2.setPalette(palette)
        self.Dato3.setPalette(palette)

        #entradas de datos
        self.initDato1 = QLineEdit(self)
        self.initDato2 = QLineEdit(self)
        self.initDato3 = QLineEdit(self)

        #boton para subir datos
        self.btnSubirDatos = QPushButton("Subida de datos", self)
        self.btnSubirDatos.clicked.connect(self.subirDatos)

        # Lista para mostrar los datos
        self.listaAnimales = QListWidget(self)

        # Layout para organizar los widgets
        layout = QGridLayout()
        #                          (y,x)
        layout.addWidget(self.Dato1,0,0)
        layout.addWidget(self.initDato1,0,1)
        layout.addWidget(self.Dato2)
        layout.addWidget(self.initDato2)
        layout.addWidget(self.Dato3)
        layout.addWidget(self.initDato3)
        layout.addWidget(self.btnSubirDatos,2,2)
        layout.addWidget(self.listaAnimales,4,0,2,4)

     

        # Asignar el layout al widget base
        basePrincipal.setLayout(layout)

        # Lista para almacenar los datos ingresados
        self.listAnimales = []

    def subirDatos(self):
        # Obtener los datos de los campos de texto
        dato1 = self.initDato1.text()
        dato2 = self.initDato2.text()
        dato3 = self.initDato3.text()

        if dato1 and dato2 and dato3:
            # Crear un string con los datos y agregarlo a la lista visual
            datosMascota = f"{dato1} - {dato2} - {dato3}"
            self.listaAnimales.addItem(datosMascota)

            # Agregar a la lista interna
            self.listAnimales.append((dato1, dato2, dato3))

            # Limpiar los campos de entrada
            self.initDato1.clear()
            self.initDato2.clear()
            self.initDato3.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = firulais()
    ventana.show()
    sys.exit(app.exec_())
