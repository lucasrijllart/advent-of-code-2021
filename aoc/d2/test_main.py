"""Tests for main module."""
import unittest

from . import main


class TestDay2(unittest.TestCase):

    inputs = []
    test_file_path = "aoc/d2/test.txt"

    def test_part_1(self):
        """Test for part 1 with example file."""
        result = main.part_1(self.test_file_path)
        self.assertEqual(result, 150)

    def test_part_2(self):
        """Test for part 1 with example file."""

    def test_parse_input(self):
        """Ensure the function returns the list of tuples that represents the input file."""
        expected_output = [("f", 5), ("d", 5), ("f", 8), ("u", 3), ("d", 8), ("f", 2)]
        data = main.parse_input(self.test_file_path)
        self.assertEqual(data, expected_output)

        

if __name__ == '__main__':
    unittest.main()