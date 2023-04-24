"""Tests for main module."""
import unittest

from . import main


class TestDay1(unittest.TestCase):

    def test_get_increasing_measurements(self):
        """Ensure the function returns the correct number of measurements that are in increasing order."""
        inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        result = main.get_increasing_measurements(inputs)
        self.assertEqual(result, 7)

    def test_part_1(self):
        """Test for part 1 with example file."""
        expected_result = 7
        result = main.part_1("aoc/d1/test.txt")
        self.assertEqual(result, expected_result)
        

if __name__ == '__main__':
    unittest.main()