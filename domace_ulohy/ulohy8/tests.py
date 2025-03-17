import unittest
from unittest.mock import patch

import vyhodnot_cestu


class TestVypoctuCeny(unittest.TestCase):

    @patch("vyhodnot_cestu.zisti_pocet_vozidiel")
    def test_najdi_najlacnejsi_sposob(self, mock_zisti_pocet_vozidiel):
        test_cases = [
            ({"Auto": 1, "autobus": 0}, 10, 20, 8),
            ({"Auto": 0, "autobus": 1}, 10, 30, 26.1),
            ({"Auto": 1, "autobus": 1}, 10, 15, 19.05),
            ({"Auto": 0, "autobus": 0}, 10, 25, 0),
        ]

        for rozlozenie_vozidiel, pocet_osob, km, cena in test_cases:
            mock_zisti_pocet_vozidiel.return_value = rozlozenie_vozidiel
            self.assertEqual(vyhodnot_cestu.vypocitaj_cenu(pocet_osob, km), cena)


if __name__ == "__main__":
    unittest.main()
