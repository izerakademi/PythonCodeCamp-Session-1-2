from oop.vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, id=None, make=None, model=None, color=None, year=None, price=None, selfBalance=None) -> None:
        super().__init__(id, make, model, color, year, price)
        self.selfBalance = selfBalance

    def setSelfBalance(self, selfBalance):
        self.selfBalance = selfBalance

    def getSelfBalance(self):
        return self.selfBalance

    def calculatePriceWithTax(self):
        return super().getPrice() * 2.02

    def __str__(self) -> str:
        return super().__str__() + "Self Balance : {selfBalance}".format(selfBalance=self.selfBalance)
