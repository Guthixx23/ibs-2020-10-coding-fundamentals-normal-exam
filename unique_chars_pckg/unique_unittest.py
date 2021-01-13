import unittest
from unique_chars_pckg.Unique import Exam

class Unique_test(unittest.TestCase):


    def test_only_unique_chars(self):
        inst = Exam()

        self.assertEqual(inst.unique_characters("abcdef"), ['a','b','c','d','e','f'])

    def test_repeated_chars(self):
        inst = Exam()

        self.assertEqual(inst.unique_characters("aabbcdeef"), ['c','d','f'])

        