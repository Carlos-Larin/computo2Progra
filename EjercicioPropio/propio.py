"""
bien esto va llegando a su final y es hora de hacer el ejercicio de manera propia
la problematica a resolver
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup,QRadioButton
from ejerciciopropio_ui import Ui_TallerCocolito  # Archivo .ui generado
import sys

class Taller(QMainWindow, Ui_TallerCocolito):
    def __init__(self):
        super(Taller, self).__init__()
        self.setupUi(self)
        
        # Conectar los cambios en los campos de texto con el cálculo del precio final
        self.inNombre_2.textChanged.connect(self.calcular_precio_final)
        self.inMano.textChanged.connect(self.calcular_precio_final)
        
        # Crear un grupo de radio buttons para gestionar las opciones de descuento
        self.radioGroup = QButtonGroup(self)
        self.radioGroup.addButton(self.radioSinDescuento)
        self.radioGroup.addButton(self.radioConDescuento)
        
        # Conectar los cambios de los radio buttons al cálculo del precio final
        self.radioSinDescuento.toggled.connect(self.calcular_precio_final)
        self.radioConDescuento.toggled.connect(self.calcular_precio_final)
        
        # Deshabilitar el campo de Precio Final para que no sea editable
        self.txtPrecioFinal.setReadOnly(True)


    def calcular_precio_final(self):
        """Calcula el precio final sumando el precio de los materiales y la mano de obra.
        Si se selecciona el descuento, se aplicará una reducción del 10% al precio final.
        """
        try:
            # Obtener los valores de los campos y asegurarse de que sean numéricos
            precio_material = float(self.inNombre_2.text()) if self.inNombre_2.text() else 0.0
            mano_obra = float(self.inMano.text()) if self.inMano.text() else 0.0
            
            # Calcular el precio base
            precio_final = precio_material + mano_obra
            
            # Verificar si el radio button de "Con descuento" está activado
            if self.radioConDescuento.isChecked():
                precio_final *= 0.9  # Aplicar un 10% de descuento

            # Mostrar el resultado en el campo de precio final
            self.txtPrecioFinal.setText(f"{precio_final:.2f}")  # Mostrar el número con 2 decimales
            
        except ValueError:
            # En caso de que no se pueda convertir el texto en número, mostrar un mensaje de error
            self.txtPrecioFinal.setText("Error")


app = QApplication(sys.argv)
ventana = Taller()
ventana.show()
sys.exit(app.exec_())