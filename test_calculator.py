import unittest
import calculator

class TestTDD1(unittest.TestCase):
    def test_calculator_dodawanie(self):
        wynik = calculator.dodawanie(2, 2)
        self.assertEqual(wynik, 4)

    def test_calculator_odejmowanie(self):
        wynik = calculator.odejmowanie(5, 2)
        self.assertEqual(wynik, 3)

    def test_calculator_mnozenie(self):
        wynik = calculator.mnozenie(5, 5)
        self.assertEqual(wynik, 25)

    def test_calculator_dzielenie(self):
        wynik = calculator.dzielenie(8, 2)
        self.assertEqual(wynik, 4)

if __name__ == '__main__':
    unittest.main()
