from src.ValidacionDatos import ValidacionDatos

class IngresoDeDatos:

    def ingresardatos(self):
        print("Ingrese los datos requeridos del trabajador")
        self.nombreTrabajador = ValidacionDatos.validar_nombre("Nombre : ")
        self.sueldoBasico = ValidacionDatos.validar_numero_decimal("Sueldo básico: ")
        self.diasFalta = ValidacionDatos.validar_numero_entero("Días de falta: ")
        self.minutosTardanza = ValidacionDatos.validar_numero_entero("Minutos de Tardanza: ")
        self.horasExtras = ValidacionDatos.validar_numero_entero("Horas extras: ")
