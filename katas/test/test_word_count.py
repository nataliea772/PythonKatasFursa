import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):
    def test_word_count_1(self):
        self.assertEqual(count_words("hello        world."), 2)

    def test_word_count_2(self):
        self.assertEqual(count_words("hello       "), 1)

    def test_word_count_3(self):
        self.assertEqual(count_words("Fursa course, 2025"), 3)
