"""
universoDC=[1,2,3,4,5,6,7,8,9,10]

def parNoDeZapatos():
   for elemento in universoDC:
      if elemento % 2==0:
         print(f"{elemento} es un numero que es divisible entre 2 por lo tanto se toma como par")
#por aqui se inoca la funcion astral de hace un momento         
parNoDeZapatos()    

Define una clase Carro con los atributos marca, modelo y año. Agrega un método que imprima la información del carro


class carro():
    marca=""
    modelo=""
    año=0

    def __init__(self):
        self.marca="Mahindra"
        self.modelo="MiniCupper"
        self.año=2004

    def mostrarDatosMovistar(self):
        print("Datos del run run")
        print(f"{self.marca} esta es la marca del carro")
        print(f"{self.modelo} este es el modelo del carro")
        print(f"El carro es  del año: {self.año}") 

carro1=carro()
carro1.mostrarDatosMovistar()  
"""

libreta = {
    "nombre": "Arthur",
    "edad": 45,
    "pueblo": "blackWater",
    "caballo": "tenesse Walker"
}


for clave, valor in libreta.items():
    print(f"Clave: {clave}, Valor: {valor}")


        