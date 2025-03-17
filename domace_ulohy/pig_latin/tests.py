import unittest

from prekladac import pig_latin


class test_pig_latin(unittest.TestCase):
    def test_pig_latin(self):
        self.assertEqual(pig_latin("hello"), "ellohay")
        self.assertEqual(pig_latin("world"), "orldway")
        self.assertEqual(pig_latin("apple"), "appleway")
        self.assertEqual(pig_latin("banana"), "ananabay")
        self.assertEqual(pig_latin("cherry"), "herrycay")
        self.assertEqual(pig_latin("eat"), "eatway")
        self.assertEqual(pig_latin("omelet"), "omeletway")


if __name__ == "__main__":
    unittest.main()
