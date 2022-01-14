import unittest
import calc
class TestCalc(unittest.TestCase):

    def test_add_integers(self):
        result = calc.add2(1,2)
        self.assertEqual(result, 3)



    def test_add_floats(self):
        result = calc.add2('10.5', 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        result = calc.add2('abc', 'def')
        self.assertEqual(result, 'abcdef')

    def test_add_string_and_integer(self):
        result = calc.add2('abc', 3)
        self.assertEqual(result, 'abc3')

    def test_add_string_and_number(self):
        result = calc.add2('abc', '5.5')
        self.assertEqual(result, 'abc5.5')

if __name__ == '__main__':
    unittest.main()