import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent1(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayCurrent2(self):
        self.assertEqual(self.g1.displayCurrent(), '_ o _ _ _ _  ')
        self.g1.guess('m')
        self.assertEqual(self.g1.displayCurrent(), 'm o _ _ _ _  ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayCurrent(), 'm o _ k _ _  ')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayCurrent(), 'm o _ k _ y  ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), 'm o _ k e y  ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayCurrent(), 'm o n k e y  ')
        
    def testDisplayGuessed1(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testDisplayGuessed2(self):
        self.assertEqual(self.g1.displayGuessed(), ' e ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayGuessed(), ' e k ')
        self.g1.guess('m')
        self.assertEqual(self.g1.displayGuessed(), ' e k m ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' e k m n ')
        self.g1.guess('o')
        self.assertEqual(self.g1.displayGuessed(), ' e k m n o ')
        self.g1.guess('y')
        self.assertEqual(self.g1.displayGuessed(), ' e k m n o y')

if __name__ == '__main__':
    unittest.main()
