"""Tests for main module."""
import unittest

from . import main


class TestDay1(unittest.TestCase):

    def test_get_increasing_measurements(self):
        """Test for part 1"""
        inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = main.get_increasing_measurements(inputs)
        self.assertEqual(result, 7)
        

if __name__ == '__main__':
    unittest.main()