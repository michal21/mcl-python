import ctypes


class Structure(ctypes.Structure):
    def __str__(self):
        return f"{self.__class__} {self.getStr()}"

    def __repr__(self):
      return str(self)