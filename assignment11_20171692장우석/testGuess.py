import unittest

from guess import *

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('chicken')
        self.g2 = Guess('duck')
    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ e _ ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), 'c _ _ c _ e _ ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayCurrent(), 'c _ _ c k e _ ')

    def testDisplayCurrnet2(self):
        self.g2.guess('d')
        self.assertEqual(self.g2.displayCurrent(), 'd _ _ _ ')
        self.g2.guess('u')
        self.assertEqual(self.g2.displayCurrent(), 'd u _ _ ')
        self.g2.guess('c')
        self.assertEqual(self.g2.displayCurrent(), 'd u c _ ')

    def testDisplayGuessed1(self):
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')

    def testDisplayGuessed2(self):
        self.g2.guess('k')
        self.assertEqual(self.g2.displayGuessed(), ' k ')
        self.g2.guess('c')
        self.assertEqual(self.g2.displayGuessed(), ' c k ')
        self.g2.guess('u')
        self.assertEqual(self.g2.displayGuessed(), ' c k u ')
        self.g2.guess('u')
        self.assertEqual(self.g2.displayGuessed(), ' c k u ')

    def testFinish(self):
        self.g1.secretWord = 'chicken'
        self.g1.currentStatus = 'chicken'
        self.assertTrue(self.g1.finished())

        self.g2.secretWord = 'duck'
        self.g2.currentStatus = 'duck'
        self.assertTrue(self.g2.finished())


if __name__ == '__main__':
    unittest.main()
