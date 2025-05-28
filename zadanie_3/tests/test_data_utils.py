import unittest
from my_awesome_lib.data_utils import remove_duplicates, flatten

class TestDataUtils(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(sorted(remove_duplicates([1,2,2,3])), [1,2,3])
    def test_flatten(self):
        self.assertEqual(flatten([[1,2],[3,4]]), [1,2,3,4])

if __name__ == "__main__":
    unittest.main()
