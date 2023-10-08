class IngresoDeDatos:

    # Ingreso de Datos
    def ingresardatos(self):
        print("Ingrese los datos requeridos del trabajador")
        self.nombreTrabajador = input("Nombre : ")
        self.sueldoBasico = float(input("sueldo basico :"))
        self.diasFalta = int(input("Dias de falta :"))
        self.minutosTardanza = int(input("Minutos de Tardanza : "))
        self.horasExtras = int(input("Horas extras :"))
