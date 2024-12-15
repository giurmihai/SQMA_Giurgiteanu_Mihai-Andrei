import unittest

class TestCase1(unittest.TestCase):
    def test_feature_a(self):
        self.assertEqual("ab", "ab")

if __name__ == "__main__":
    unittest.main()