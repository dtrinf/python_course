
# https://coverage.readthedocs.io/en/6.3/
# https://docs.python.org/3.8/library/unittest.html#unittest.TestCase.setUpClass

import unittest

from Geometria_.model.Geometria import Geometria

class GeometriaTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.g = Geometria(2.00, 3.10, 4.00)

    def testAreaCuadrado(self):
        self.assertEqual(self.g.switch(1), 4.0, "OK")

    def testAreaCirculo(self):
        self.assertEqual(self.g.switch(2), 12.5664, "OK")

    def testAreaTiangulo(self):
        self.assertEqual(self.g.switch(3), 3.1, "OK")

    def testAreaRectangulo(self):
        self.assertEqual(self.g.switch(4), 6.2, "OK")

    def testAreaPentagono(self):
        self.assertEqual(self.g.switch(5), 3.1, "OK")

    def testAreaRombo(self):
        self.assertEqual(self.g.switch(6), 3.1, "OK")

    def testAreaRomboide(self):
        self.assertEqual(self.g.switch(7), 6.2, "OK")

    def testAreaTrapecio(self):
        self.assertEqual(self.g.switch(8), 10.2, "OK")

    def testSet_figuraName(self):
        for menu_option in range(1, 9):
            with self.subTest(menu_option=menu_option):
                self.g.set_figuraName(menu_option)
                self.assertIn(self.g.figuraName, ["Cuadrado", "Circulo", "Tiangulo", "Rectangulo", "Pentagono", "Rombo", "Romboide", "Trapecio"])
            if menu_option == 1:
                self.assertEqual(self.g.figuraName, "Cuadrado")
            elif menu_option == 2:
                self.assertEqual(self.g.figuraName, "Circulo")
            elif menu_option == 3:
                self.assertEqual(self.g.figuraName, "Tiangulo")
            elif menu_option == 4:
                self.assertEqual(self.g.figuraName, "Rectangulo")
            elif menu_option == 5:
                self.assertEqual(self.g.figuraName, "Pentagono")
            elif menu_option == 6:
                self.assertEqual(self.g.figuraName, "Rombo")
            elif menu_option == 7:
                self.assertEqual(self.g.figuraName, "Romboide")
            elif menu_option == 8:
                self.assertEqual(self.g.figuraName, "Trapecio")


    @classmethod
    def tearDownClass(self):
        del self.g