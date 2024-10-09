import unittest
from src.word_frequency import compute_word_frequency, read_input_file

class TestWordFrequency(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(compute_word_frequency(""), {})

    def test_single_word(self):
        self.assertEqual(compute_word_frequency("hello"), {"hello": 1})

    def test_repeated_word(self):
        self.assertEqual(compute_word_frequency("hello hello"), {"hello": 2})

    def test_multiple_words(self):
        text = "hello world hello"
        expected = {"hello": 2, "world": 1}
        self.assertEqual(compute_word_frequency(text), expected)

    def test_case_insensitivity(self):
        text = "Hello hello HeLLo"
        expected = {"hello": 3}
        self.assertEqual(compute_word_frequency(text), expected)

    def test_punctuation(self):
        text = "hello, world! hello."
        expected = {"hello": 2, "world": 1}
        self.assertEqual(compute_word_frequency(text), expected)

if __name__ == "__main__":
    unittest.main()
