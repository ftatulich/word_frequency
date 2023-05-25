import unittest

from main import word_frequency


class WordFrequencyTestCase(unittest.TestCase):
    def test_empty_paragraph(self):
        result = word_frequency([])
        self.assertEqual(result, {})

    def test_single_sentence(self):
        paragraph = ['Hello world!']
        result = word_frequency(paragraph)
        expected = {'hello': 1, 'world': 1}
        self.assertEqual(result, expected)

    def test_multiple_sentences(self):
        paragraph = ['This is a test.', 'Test sentence.']
        result = word_frequency(paragraph)
        expected = {'this': 1, 'is': 1, 'a': 1, 'test': 2, 'sentence': 1}
        self.assertEqual(result, expected)

    def test_sentence_with_punctuation(self):
        paragraph = ['I like apples, bananas, and oranges.']
        result = word_frequency(paragraph)
        expected = {'i': 1, 'like': 1, 'apples': 1, 'bananas': 1, 'and': 1, 'oranges': 1}
        self.assertEqual(result, expected)

    def test_sentence_with_duplicate_words(self):
        paragraph = ['Hello world, hello world!']
        result = word_frequency(paragraph)
        expected = {'hello': 2, 'world': 2}
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        paragraph = ['HELLO', 'Hello', 'hello']
        result = word_frequency(paragraph)
        expected = {'hello': 3}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
