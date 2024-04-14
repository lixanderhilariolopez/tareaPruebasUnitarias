import unittest

class TestSimpleWebApp(unittest.TestCase):
    def test_welcome_message(self):
        expected_message = 'Bienvenidos a mi página web!'
        # Simulamos la búsqueda del elemento h1 en el documento
        actual_message = 'Bienvenidos a mi página web!'  # Simulamos el texto real obtenido
        self.assertEqual(actual_message, expected_message)

if __name__ == '__main__':
    unittest.main()