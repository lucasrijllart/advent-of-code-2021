"""Tests for main module."""
import unittest

from . import main


class TestDay1(unittest.TestCase):

    inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    test_file_path = "aoc/d1/test.txt"

    def test_part_1(self):
        """Test for part 1 with example file."""
        result = main.part_1(self.test_file_path)
        self.assertEqual(result, 7)

    def test_part_2(self):
        """Test for part 1 with example file."""
        result = main.part_2(self.test_file_path)
        self.assertEqual(result, 5)

    def test_parse_input(self):
        """Ensure the function returns the integer list representation of a test file."""
        expected_output = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        data = main.parse_input(self.test_file_path)
        self.assertEqual(data, expected_output)

    def test_get_increasing_measurements(self):
        """Ensure the function returns the correct number of measurements that are in increasing order."""
        result = main.get_increasing_measurements(self.inputs)
        self.assertEqual(result, 7)

    def test_get_increasing_sliding_window(self):
        """Ensure the function returns the correct number of measurements that are increasing in the sliding window."""
        result = main.get_increasing_sliding_window(self.inputs)
        self.assertEqual(result, 5)


        

if __name__ == '__main__':
    unittest.main()