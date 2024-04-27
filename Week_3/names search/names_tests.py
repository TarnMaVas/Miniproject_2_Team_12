from names import find_names
from working_names import find_names as working_find_names
import unittest

# names.py
path = 'boy_names.txt'
class TestFindNames(unittest.TestCase):
    
    def test_most_popular_names(self):
        # Test the first element of the tuple (most popular names)
        # Example: Check if the top 3 names are correctly returned
        names = find_names(path)[0]
        expected_names = working_find_names(path)[0]
        self.assertEqual(names, expected_names)

    def test_names_used_once(self):
        # Test the second element of the tuple (names used only once)
        # Example: Check if the count and set of unique names are correct
        _, (count, unique_names), _ = find_names(path)
        expected_count = working_find_names(path)[1][0]
        expected_unique_names = working_find_names(path)[1][1]
        self.assertEqual(count, expected_count)
        self.assertEqual(unique_names, expected_unique_names)

    def test_most_popular_first_letter(self):
        # Test the third element of the tuple (most popular first letter)
        # Example: Check if the letter 'A' and associated names are correct
        _, _, (letter, letter_names, num_children) = find_names(path)
        expected_letter = working_find_names(path)[2][0]
        expected_letter_names = working_find_names(path)[2][1]
        expected_num_children = working_find_names(path)[2][2]
        self.assertEqual(letter, expected_letter)
        self.assertEqual(letter_names, expected_letter_names)
        self.assertEqual(num_children, expected_num_children)

if __name__ == "__main__":
    unittest.main()