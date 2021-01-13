import unittest
from unique_chars_pckg.Unique import Exam


class Unique_test(unittest.TestCase):

    # test for unique characters in teh string only
    def test_only_unique_chars(self):
        inst = Exam()

        self.assertEqual(inst.unique_characters("abcdef"), ['a', 'b', 'c', 'd', 'e', 'f'])

    # test for repeated characters in the string too
    def test_repeated_chars(self):
        inst = Exam()

        self.assertEqual(inst.unique_characters("aabbcdeef"), ['c', 'd', 'f'])
