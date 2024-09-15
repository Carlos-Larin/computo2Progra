"""
bien esto va llegando a su final y es hora de hacer el ejercicio de manera propia
la problematica a resolver es de un taller de estructura metalica que ocupan facturar a los clientes el precio de sus trabajos
y marcando la mano de obra y el precio del costo del material usado(hierros, pintura, electrodos, etc.)
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup,QRadioButton
from PyQt5.QtGui import QFont, QPalette, QColor,QIcon
from ejerciciopropio_ui import Ui_TallerCocolito  # Archivo .ui generado
import sys

class Taller(QMainWindow, Ui_TallerCocolito):
    def __init__(self):
        super(Taller, self).__init__()
        self.setupUi(self)

        fondocolor=QPalette()
        fondocolor.setColor(QPalette.Window,QColor(219, 145, 225))
        self.setPalette(fondocolor)
        #no me funciono el logo Pipipi
        self.setWindowIcon(QIcon('casajp.png'))
        
        # Conectar los cambios en los campos de texto con el cálculo del precio final
        self.inNombre_2.textChanged.connect(self.calcularPrecioFinal)
        self.inMano.textChanged.connect(self.calcularPrecioFinal)
        
        # Crear un grupo de radio buttons para gestionar las opciones de descuento
        self.radioGroup = QButtonGroup(self)
        self.radioGroup.addButton(self.radioSinDescuento)
        self.radioGroup.addButton(self.radioConDescuento)
        
        # Conectar los cambios de los radio buttons al cálculo del precio final
        self.radioSinDescuento.toggled.connect(self.calcularPrecioFinal)
        self.radioConDescuento.toggled.connect(self.calcularPrecioFinal)
        
        # Deshabilitar el campo de Precio Final para que no sea editable
        self.txtPrecioFinal.setReadOnly(True)


    def calcularPrecioFinal(self):
        """Calcula el precio final sumando el precio de los materiales y la mano de obra.
        Si se selecciona el descuento, se aplicará una reducción del 10% al precio final.
        Este descuento solo lo aplican para clientes frecuentes del taller.
        """
        try:
            # Obtener los valores de los campos y asegurarse de que sean numéricos
            precioMaterial = float(self.inNombre_2.text()) if self.inNombre_2.text() else 0.0
            mano_obra = float(self.inMano.text()) if self.inMano.text() else 0.0
            
            # Calcular el precio base
            precioFinal = precioMaterial + mano_obra
            
            # Verificar si el radio button de "Con descuento" está activado
            if self.radioConDescuento.isChecked():
                precioFinal *= 0.9  # Aplicar un 10% de descuento

            # Mostrar el resultado en el campo de precio final
            self.txtPrecioFinal.setText(f"{precioFinal:.2f}")  # Mostrar el número con 2 decimales
            
        except ValueError:
            # En caso de que no se pueda convertir el texto en número, mostrar un mensaje de error
            self.txtPrecioFinal.setText("Error")


app = QApplication(sys.argv)
ventana = Taller()
ventana.show()
sys.exit(app.exec_())