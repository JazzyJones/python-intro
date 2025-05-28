import unittest
from app import is_email_valid, rectangle_area, filter_even, convert_date, is_palindrome

class TestApp(unittest.TestCase):
    def test_is_email_valid(self):
        self.assertTrue(is_email_valid("test@example.com"))
        self.assertFalse(is_email_valid("test.example.com"))
        self.assertFalse(is_email_valid("test@.com"))

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(-1, 5), -5)

    def test_filter_even(self):
        self.assertEqual(filter_even([1,2,3,4]), [2,4])
        self.assertEqual(filter_even([]), [])
        self.assertEqual(filter_even([1,3,5]), [])

    def test_convert_date(self):
        self.assertEqual(convert_date("31-12-2020"), "2020/12/31")
        with self.assertRaises(ValueError):
            convert_date("31/12/2020")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Kajak"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Python"))

if __name__ == '__main__':
    unittest.main()
