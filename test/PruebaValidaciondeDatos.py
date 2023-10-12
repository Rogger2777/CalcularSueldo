import unittest
from src.ValidacionDatos import ValidacionDatos


class TestValidacionDatos(unittest.TestCase):
    def test_validar_numero_entero(self):
        # Prueba con numero entero positivo
        resultado = ValidacionDatos.validar_numero_entero("Ingrese un número entero positivo: ")
        self.assertEqual(resultado, 42)

        # Prueba con numero entero negativo
        resultado = ValidacionDatos.validar_numero_entero("Ingrese un número entero negativo: ")
        self.assertEqual(resultado, -1)  # Esto debería fallar

        # Prueba con numero decimal (esto  falla)
        with self.assertRaises(ValueError):
            ValidacionDatos.validar_numero_entero("Ingrese un número decimal: ")

    def test_validar_numero_decimal(self):
        # Prueba con numero decimal positivo
        resultado = ValidacionDatos.validar_numero_decimal("Ingrese un número decimal positivo: ")
        self.assertEqual(resultado, 3.14)

        # Prueba con número decimal negativo
        resultado = ValidacionDatos.validar_numero_decimal("Ingrese un número decimal negativo: ")
        self.assertEqual(resultado, -2.5)  # Esto deberia fallar

        # Prueba con número entero (esto falla)
        with self.assertRaises(ValueError):
            ValidacionDatos.validar_numero_decimal("Ingrese un número entero: ")

    def test_validar_nombre(self):
        # Prueba con nombre valido
        resultado = ValidacionDatos.validar_nombre("Ingrese un nombre válido: ")
        self.assertEqual(resultado, "Juan")

        # Prueba con nombre que contiene números (esto debería fallar)
        with self.assertRaises(ValueError):
            ValidacionDatos.validar_nombre("Ingrese un nombre inválido: Juan123")

        # Prueba con nombre que contiene caracteres especiales (falla)
        with self.assertRaises(ValueError):
            ValidacionDatos.validar_nombre("Ingrese un nombre inválido: María!")

if __name__ == '__main__':
    unittest.main()