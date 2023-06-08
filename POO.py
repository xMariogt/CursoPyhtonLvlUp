class Casa():
    color = 'amarillo'
    numeracion = None
    frente = '10 metros'
    fondo = '20 metros'
    dueño = None

    def pintar(self, nuevo_color):
        self.color = nuevo_color
    
    def vender(self, nuevo_dueño):
        self.dueño = nuevo_dueño
        return 'venta exitosa.'

casa1 = Casa()
#print(type(casa1))
print(casa1.color)
print(casa1.numeracion)
casa1.numeracion = 'A1'
print(casa1.numeracion)
casa1.pintar('rojo')
print(casa1.color)


