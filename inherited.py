from base import Base


class Inherited(Base):
    def _init_(self):
        super(Inherited, self)._init_()

    def read(self):
        self.a = 1
        return "actual"

    def setUp(self, variable):
        self.variable = "a"
        super(B, self).setUp(variable = variable)
