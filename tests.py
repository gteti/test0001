import unittest

from run import *


class TestNumbers(unittest.TestCase):

    def test_integers(self):
        """
        this test asserts the sum of the numbers is of type integer
        """
        self.assertTrue(type(sumOfNumbers(1,2)) is int)
    
    def test_sum(self):
        """
        this test asserts the sum of the tested values equates to 3
        """
        self.assertEqual(sumOfNumbers(1,2), 3)

    def test_sum2(self):
        """
        this test asserts the sum of the tested values is equals to 4
        """
        self.assertEqual(sumOfNumbers(1,2), 4)


if __name__ == "__main__":
    unittest.main()
