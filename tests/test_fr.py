import unittest

from mcl import Fr


class FrTests(unittest.TestCase):
    def testInitFr(self):
        self.assertIsNotNone(Fr())

    def testSetStr(self):
        Fr().setStr("12345678901234567")

    def testIsEqual(self):
        l = Fr()
        l.setByCSPRNG()
        self.assertTrue(l == l)

    def testSetInt(self):
        Fr().setInt(1)

    def testMul(self):
        Fr() * Fr()

    def testGetStr(self):
        fr = Fr()
        fr.setStr("255")
        s = fr.getStr()
        self.assertEqual("255", s)

    def testByCSPRNG(self):
        Fr().setByCSPRNG()
