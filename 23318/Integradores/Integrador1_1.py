from Integrador1 import Cuenta
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad = 0, bonificacion = 0, edad = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    def mostrar(self):
        return 'Cuenta Joven\n' + 'Titular: ' + self.titular + '\nCantidad: ' + str(self.cantidad) + '\nBonificacion: ' + str(self.bonificacion) + '%'
    
    def es_titular_valido(self):
        return self.edad < 25 and self.edad >= 18
    
    def retirar(self, cantidad):
        if not self.es_titular_valido():
            print ('El titular no es válido para retirar dinero')
        elif cantidad > 0:
            super().retirar(cantidad)
            print ('Retiro exitoso')

# cuenta_uno = CuentaJoven('Lopez', 200, 15, 17)
# print(cuenta_uno.mostrar())
# print(cuenta_uno.es_titular_valido())
# print(cuenta_uno.retirar(100))
# print(cuenta_uno.cantidad)

# cuenta_dos = CuentaJoven('Perez', 300, 10, 20)
# print(cuenta_dos.mostrar())
# print(cuenta_dos.es_titular_valido())
# print(cuenta_dos.retirar(150))
# print(cuenta_dos.cantidad)    