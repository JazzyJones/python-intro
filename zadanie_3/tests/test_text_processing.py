import unittest
from my_awesome_lib.text_processing import count_words, reverse_text

class TestTextProcessing(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Ala ma kota"), 3)
    def test_reverse_text(self):
        self.assertEqual(reverse_text("abc"), "cba")

if __name__ == "__main__":
    unittest.main()
