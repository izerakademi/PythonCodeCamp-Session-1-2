from oop.vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, id=None, make=None, model=None, color=None, year=None, price=None, airSuspension=None) -> None:
        super().__init__(id, make, model, color, year, price)
        self.airSuspension = airSuspension

    def setAirSuspension(self, airSuspension):
        self.airSuspension = airSuspension

    def getAirSuspension(self):
        return self.airSuspension

    def calculatePriceWithTax(self):
        return super().getPrice() * 1.87

    def __str__(self) -> str:
        return super().__str__() + "Air Suspension : {airSuspension}".format(airSuspension=self.airSuspension)
