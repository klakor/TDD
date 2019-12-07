import unittest
import mojprogram

class TestTDD1(unittest.TestCase):
    def test_zwroc_100(self):
        wynik = mojprogram.zwroc_100()
        self.assertEqual(wynik, 100)

    def test_zwroc_parametr(self):
        wynik = mojprogram.zwroc_parametr(124)
        self.assertEqual(wynik, 124)
        wynik = mojprogram.zwroc_parametr(23)
        self.assertEqual(wynik, 23)

if __name__ == '__main__':
    unittest.main()
