from oop.vehicle import Vehicle


# Inheritance - Miras
class Car(Vehicle):
    def __init__(self, id=None, make=None, model=None, color=None, year=None, price=None, sunroof=None) -> None:
        super().__init__(id, make, model, color, year, price)
        self.sunroof = sunroof

    def setSunroof(self, sunroof):
        self.sunroof = sunroof

    def getSunroof(self):
        return self.sunroof

    def calculatePriceWithTax(self):
        return super().getPrice() * 1.64

    def __str__(self) -> str:
        return super().__str__() + "Sunroof : {sunroof}".format(sunroof=self.sunroof)

