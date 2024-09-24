
class Sucursal1059():
    id_sucursal=0
    Nombre=""
    Direccion=""
    Numero=""
    Horario=""
    Correo=""
    Ingresos=0

    def mostrardatos(self):
        print(f"ID de la sucursal: {self.id_sucursal}")
        print(f"Nombre de la sucursal: {self.Nombre}")
        print(f"Direccion de la sucursal: {self.Direccion} ")
        print(f"Numero de la sucursal: {self.Numero}")
        print(f"Horario de la sucursal: {self.Horario}")
        print(f"Correo de la sucursal: {self.Correo}")
        print(f"Ingresos de la sucursal: {self.Ingresos} ")
    
    def lista_sucursal(self):
        nombre = ["Torres","Riveras","Zaragoza","Las haciendas","Anapra"]
        for l in nombre:
            print(l)
    
    def tupla_sucursal(self):
        gerente = ("Jose","Martin","Sofia","Carmen","Maria")
        for g in gerente:
            print(g)

    def diccionario_sucursal(self):
        ingresos = {
            "Sucursal 1:" : "1300",
            "Sucursal 2:" : "19000",
            "Sucursal 3:" : "1500",
            "Sucursal 4:" : "13000",
            "Sucursal 5:" : "12400"
        }
        for a,b in ingresos.items ():
            print(a,b)
    
    def ingresos(self):
        print("Los ingresos de la sucursal se realizaron correctamente")
        
    def bajaingresos(self):
        print("Los ingresos de las sucursal se realizo incorrectamente")

Productos_artesanales=Sucursal1059()

Productos_artesanales.id_sucursal=1
Productos_artesanales.Nombre="Libella"
Productos_artesanales.Direccion="Gomez Morin"
Productos_artesanales.Numero="6562345678"
Productos_artesanales.Horario="7:00am - 10:00pm"
Productos_artesanales.Correo="libella08@gmail.com"
Productos_artesanales.Ingresos=3456


print("\nMostrar Datos")
Productos_artesanales.mostrardatos()

print("\nLista de sucursales")
Productos_artesanales.lista_sucursal()

print("\nTupla de gerentes de las sucursales")
Productos_artesanales.tupla_sucursal()

print("\nDiccionario ingresos de sucursales")
Productos_artesanales.diccionario_sucursal()

print("\n Funcion Ingresos de sucursales")
Productos_artesanales.ingresos()

print("\n Funcion bajas de ingresos de sucursales")
Productos_artesanales.bajaingresos()