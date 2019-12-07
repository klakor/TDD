import unittest
import helloworld

class TestTDD1(unittest.TestCase):
    def test_hello_world(self):
        wynik = helloworld.print_hello()
        self.assertEqual(wynik, "Hello world")

if __name__ == '__main__':
    unittest.main()
