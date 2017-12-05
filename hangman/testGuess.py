import unittest

from guess import Guess
from wordDics import*

class TestGuess(unittest.TestCase):
    def setUp(self):
        self.gList = [Guess('default'), Guess('apple'), Guess('j o y')]

    def tearDown(self):
        pass

    def toString(self, k):
        kList = []
        retStr = ""

        kList += k
        kList.sort()
        for i in kList:
            retStr += i
            retStr += " "
        return retStr

    ##i는 인덱스
    ##j는 리스트
    ##k는 dic의 key
    def testDisplayCurrent(self):
        for i in range(len(self.gList)):
            for j in gDicKeys:
                for k in j:
                    self.gList[i].guess(k)
                    self.assertEqual(self.gList[i].displayCurrent(), gDics[i][k])

    def testDisplayGuessed(self):
        for i in range(len(self.gList)):
            for j in gDicKeys:
                for k in j:
                    self.gList[i].guess(k)
                    ##k를 리스트에 넣어 정렬한 후 스트링에 넣어 리턴하는 함수
                    self.assertEqual(self.gList[i].displayGuessed(), self.toString(k))

"""
    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
"""
if __name__ == '__main__':
    unittest.main()
