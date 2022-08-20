import Code_Coverage.mymath as mymath
import unittest


class TestAdd(unittest.TestCase):

    def test_add_integer(self):
        result = mymath.add(10, 5)
        self.assertEqual(result, 15)

    def test_sub_integer(self):
        result = mymath.subtraction(10, 5)
        self.assertEqual(result, 5)

    def test_multiply_integer(self):
        result = mymath.multiplication(10, 5)
        self.assertEqual(result, 50)

    def test_add_float(self):
        result = mymath.add(10.5, 5)
        self.assertEqual(result, 15.5)


if __name__ == '__main__':
    unittest.main()
