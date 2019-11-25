# Jackson J.
# 11/23/19
# This will be the Car class


class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def description(self):
        return self.make + ' and the model is ' + self.model + ". " + self.make + " was made in " + self.year + " and reaches a top speed of " + self.speed + " mph."
