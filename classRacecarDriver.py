from classCar import Car
from classPerson import Person


class RacercarDriver:

    def __init__(self, first, last, age, weight, height, trophies, make, model, year, speed):
        self.driver = Person(first, last, age, weight, height)
        self.trophies = trophies
        self.racercar = Car(make, model, year, speed)

    def info(self):
        print(f"Here we have the {self.racercar.description()}")
        print(f"The driver of this car is {self.driver.first}")
        print(self.driver)
