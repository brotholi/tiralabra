import unittest
from services.damerau_levenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.damerau_levenshtein = DamerauLevenshtein()
        self.word1 = "kissa"
        self.word2 = "kissoja"

    def test_distance(self):
        self.assertEqual(self.damerau_levenshtein.distance(
            self.word1, self.word2), 2)
        self.assertEqual(
            self.damerau_levenshtein.distance("kissa", "kissa"), 0)

    def test_distance_with_empty_string(self):
        self.assertEqual(
            self.damerau_levenshtein.distance("", "kissa"), 5)
        self.assertEqual(
            self.damerau_levenshtein.distance("kissa", ""), 5)
        self.assertEqual(
            self.damerau_levenshtein.distance("", ""), 0)

    def test_distance_with_none(self):
        self.assertEqual(
            self.damerau_levenshtein.distance(None, "kissa"), 5)
        self.assertEqual(
            self.damerau_levenshtein.distance("kissa", None), 5)
        self.assertEqual(
            self.damerau_levenshtein.distance(None, None), 0)
