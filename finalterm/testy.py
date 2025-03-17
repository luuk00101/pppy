import unittest
from unittest.mock import patch, mock_open
from utvar import Kruh
import math


class TestKruh(unittest.TestCase):

    def setUp(self):
        self.kruh = Kruh(5)
        self.assertEqual(self.kruh.polomer, 5)

    def test_zmena_polomeru(self):
        self.kruh.polomer = 10
        self.assertEqual(self.kruh.polomer, 10)

    def test_zmena_polomeru_text(self):
        with self.assertRaises(TypeError):
            self.kruh.polomer = "desat"

    def test_zmena_polomeru_zaporne(self):
        with self.assertRaises(ValueError):
            self.kruh.polomer = -5

    def test_obsah_kruhu(self):
        kruh = Kruh(5)

        vysledok = math.pi * 5**2
        self.assertAlmostEqual(self.kruh.obsah(), vysledok)

    @patch("builtins.open", new_callable=mock_open, read_data="Kruh(5)")
    def test_kruh_zo_suboru(self, mock_file):
        subor = "kruh.txt"
        kruh = Kruh.kruh_zo_suboru(subor)
        self.assertEqual(kruh.polomer, 5)


if __name__ == "__main__":
    unittest.main()
