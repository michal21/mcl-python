import unittest

from mcl import GT
from mcl import G2
from mcl import G1
from mcl import Fr

from . import test_data


class GTTests(unittest.TestCase):
    def testInitGT(self):
        self.assertIsNotNone(GT())

    def testPairing(self):
        fr1 = Fr.rand()
        g1 = G1(test_data.G1_STR)
        g2 = G2(test_data.G2_STR)
        fr2 = Fr.rand()
        gt = GT.pairing(g1 * fr1, g2 * fr2)
        self.assertIsNotNone(gt)

    def testHashAndMapTo(self):
        g1 = G1.hashAndMapTo(b"test")
        g2 = G2.hashAndMapTo(b"test")
        gt = GT.hashAndMapTo(b"test")
        self.assertEqual(gt, GT.pairing(g1, g2))

    def testStr(self):
        gt1 = GT.hashAndMapTo(b'asdf')
        gt2 = GT(gt1.getStr())
        self.assertEqual(gt1, gt2)
