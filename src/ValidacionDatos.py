class ValidacionDatos:
    @staticmethod
    def validar_numero_entero(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= 0:
                    return valor
                else:
                    print("ERROR! No se permiten valores negativos")
            except ValueError:
                print("¡Error! Debes ingresar un número entero.")

    @staticmethod
    def validar_numero_decimal(mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor >= 0:
                    return valor
                else:
                    print("Error! No se permiten valores negativos")
            except ValueError:
                print("¡Error! Debes ingresar un número decimal.")

    @staticmethod
    def validar_nombre(mensaje):
        while True:
            nombre = input(mensaje)
            if nombre.isalpha():
                return nombre
            else:
                print("¡Error! El nombre solo debe contener letras.")
