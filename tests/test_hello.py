import unittest

from src.hello import greet


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), "Hello, World!")

    def test_custom_name(self):
        self.assertEqual(greet("GitLab"), "Hello, GitLab!")


if __name__ == "__main__":
    unittest.main()
