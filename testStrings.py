import unittest
import stringProgram

class Test(unittest.TestCase):
    def test_string_upper(self):
        wynik = stringProgram.upper("hello world")
        self.assertEqual(wynik, "Hello World")

    def test_string_swapcase(self):
        wynik = stringProgram.swapcase("Hello World")
        self.assertEqual(wynik, "hELLO wORLD")

    def test_string_join(self):
        wynik = stringProgram.join("Hello World")
        self.assertEqual(wynik, "HelloWorld")

    def test_string_isalpha(self):
        wynik = stringProgram.isalpha("Hello World")
        self.assertTrue(wynik)

    def test_string_endswith(self):
        wynik = stringProgram.endswith("Hello World")
        self.assertEqual(wynik, "World")

if __name__ == '__main__':
    unittest.main()


#upper()	Converts a string into upper case
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#join()	Joins the elements of an iterable to the end of the string
#isalpha()	Returns True if all characters in the string are in the alphabet
#endswith()	Returns true if the string ends with the specified value
