# Importamos las clasese desde sus respectivos modulos
from src.IngresoDatos import IngresoDeDatos
from src.CalculoSueldoPagar import CalcularSueldo
from src.ImprimeBoletaPago import ImprimirBoleta

if __name__ == '__main__':
    # Crea una instancia de la clase ingresodatos
    datos = IngresoDeDatos()
    # Llama al metodo para ingreso de datos
    datos.ingresardatos()

    # Obtinene los datos ingresados
    sueldoBasico = datos.sueldoBasico
    horasExtras = datos.horasExtras
    diasFalta = datos.diasFalta
    minutosTardanza = datos.minutosTardanza

    # Crear una instancia de la clase CalcularSueldo
    calcular = CalcularSueldo(sueldoBasico, horasExtras, diasFalta, minutosTardanza)
    bonificacion = calcular.calculoBonificaciones()
    descuentos = calcular.calculoDescuento()
    sueldoNeto = calcular.calculoSueldoNeto()
    renumeracionMinima = calcular.remuneracionMinima()

    # Imprimimos boleta de pago
    boletaDePago = ImprimirBoleta(sueldoBasico, bonificacion, descuentos, sueldoNeto, renumeracionMinima)
    boletaDePago.ImprimirResultados()
