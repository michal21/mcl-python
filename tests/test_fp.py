import unittest

from mcl import Fp


class FpTests(unittest.TestCase):
    def testInitFp(self):
        self.assertIsNotNone(Fp())

    def testSetByCSPRNG(self):
        Fp().setByCSPRNG()

    def testAdd(self):
        Fp() + Fp()

    def testSub(self):
        Fp() - Fp()

    def testMul(self):
        Fp() * Fp()

    def testDiv(self):
        Fp() / Fp()

    def testNeg(self):
        not Fp()

    @unittest.skip("inv not yet implemented for FP")
    def testInv(self):
        pass

    def testSerialization(self):
        Fp().serialize()

    @unittest.skip("setHashOf not yet implemented for FP")
    def testSetHashOf(self):
        pass

    @unittest.skip("mapToG1 not yet implemented for FP")
    def testMapToG1(self):
        pass

    def testStr(self):
        fp = Fp()
        fp.setStr(b"255")
        s = fp.getStr()
        self.assertEqual(b"255", s)

    def testSetInt(self):
        Fp().setInt(1)
