from .. import utils
from .. import builder
from . import base
from .G1 import G1
from .G2 import G2
from .Fp import Fp
from .Fr import Fr


@builder.provide_methods(
    builder.method("__add__").using(builder.buildThreeOp).with_args("add"),
    builder.method("__eq__").using(builder.buildIsEqual),
    builder.method("__invert__").using(builder.buildTwoOp).with_args("inv"),
    builder.method("__mul__").using(builder.buildThreeOp).with_args("mul"),
    builder.method("__neg__").using(builder.buildTwoOp).with_args("neg"),
    builder.method("__pow__").using(builder.buildPow).with_args(Fr),
    builder.method("__sub__").using(builder.buildThreeOp).with_args("sub"),
    builder.method("deserialize"),
    builder.method("getStr"),
    builder.method("isZero"),
    builder.method("pairing").using(builder.buildPairing).with_args(G1, G2),
    builder.method("serialize"),
    builder.method("setStr"),
)
class GT(base.Structure):
    _fields_ = [
        ("d", (Fp * 12)),
    ]

    def __init__(self, s=None):
        if s is not None:
            self.setStr(s)

    def hashAndMapTo(x):
        return GT.pairing(G1.hashAndMapTo(x), G2.hashAndMapTo(x))
