import unittest
from unittest.mock import patch


import subor


class TestZipsovania(unittest.TestCase):

    def mock_citaj_data(subor):
        if subor == "subor1":
            return [1, 3]
        elif subor == "subor2":
            return [2, 4]

    @patch("subor.zapis_data")
    @patch("subor.citaj_data", side_effect=mock_citaj_data)
    def test_zozipsuj(self, mock_citaj_data, mock_zapis_data):

        subor.zozipsuj("subor1", "subor2", "subor_out")

        mock_citaj_data.assert_any_call("subor1")
        mock_citaj_data.assert_any_call("subor2")

        mock_zapis_data.assert_called_once_with("subor_out", [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
