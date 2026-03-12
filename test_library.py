import unittest
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library(["Python", "AI Basics"], "Test Library")

    def test_add_book(self):
        result = self.lib.addBook("Data Science")
        self.assertEqual(result, "Book added successfully.")

    def test_duplicate_book(self):
        result = self.lib.addBook("Python")
        self.assertEqual(result, "Book already exists.")


if __name__ == "__main__":
    unittest.main()