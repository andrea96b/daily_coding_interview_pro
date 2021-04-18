import unittest
from daily837 import SentenceChecker

class Test837(unittest.TestCase):

    def test_1(self):
        self.checker = SentenceChecker()
        self.assertTrue(self.checker.check('This, is a correct sentence.'))

    def test_2(self):
        self.checker = SentenceChecker()
        self.assertFalse(self.checker.check('This, is a wrong  sentence.'))

    def test_3(self):
        self.checker = SentenceChecker()
        self.assertTrue(self.checker.check('A good sentence?'))

    def test_4(self):
        self.checker = SentenceChecker()
        self.assertFalse(self.checker.check('A good sentence ?'))

if __name__ == '__main__':
    unittest.main()